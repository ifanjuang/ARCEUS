"""
AgentService — boucle agentique ReAct (Reason + Act).

Fonctionnement :
  1. Reçoit une instruction + contexte affaire
  2. Envoie au LLM avec les outils disponibles (function calling)
  3. Si le LLM appelle un outil → exécute → réinjecte le résultat
  4. Répète jusqu'à réponse finale ou max_iterations atteint
  5. Persiste l'historique complet dans agent_runs
"""
import json
import time
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from core.logging import get_logger
from core.services.llm_service import LlmService
from core.settings import settings
from modules.agent.models import AgentRun
from modules.agent.tools import DEFINITIONS, execute_tool

log = get_logger("agent.service")

SYSTEM_PROMPT = """Tu es un assistant copilote pour une agence d'architecture (MOE).
Tu aides les chargés de projet à trouver des informations, analyser des documents
et prendre des décisions sur leurs projets de construction.

Règles :
- Utilise les outils disponibles pour chercher les informations avant de répondre.
- Cite tes sources (nom du document, score de pertinence).
- Réponds en français, de manière concise et structurée.
- Si une information est introuvable, dis-le clairement.
- N'invente jamais de données chiffrées (délais, coûts, surfaces).
"""


async def run_agent(
    db: AsyncSession,
    instruction: str,
    affaire_id: UUID,
    user_id: UUID | None,
    max_iterations: int = 10,
) -> AgentRun:
    """Exécute la boucle agentique et persiste le résultat."""
    t_start = time.monotonic()

    run = AgentRun(
        affaire_id=affaire_id,
        user_id=user_id,
        instruction=instruction,
        status="running",
        steps=[],
    )
    db.add(run)
    await db.flush()  # obtenir l'id sans commit

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": instruction},
    ]

    steps: list[dict] = []
    final_answer: str | None = None
    model = settings.effective_llm_model

    try:
        for iteration in range(max_iterations):
            t_iter = time.monotonic()

            # Appel LLM avec les outils
            response = await LlmService._get_client().chat.completions.create(
                model=model,
                messages=messages,
                tools=DEFINITIONS,
                tool_choice="auto",
                temperature=0.3,
                max_tokens=2048,
            )

            choice = response.choices[0]
            msg = choice.message

            # Ajouter la réponse du LLM aux messages
            messages.append(msg.model_dump(exclude_none=True))

            # Pas d'appel d'outil → réponse finale
            if not msg.tool_calls:
                final_answer = msg.content or ""
                break

            # Exécuter tous les appels d'outils demandés
            for tc in msg.tool_calls:
                t_tool = time.monotonic()
                tool_name = tc.function.name
                tool_args = json.loads(tc.function.arguments or "{}")

                log.info(
                    "agent.tool_call",
                    run_id=str(run.id),
                    iteration=iteration,
                    tool=tool_name,
                    args=tool_args,
                )

                tool_output = await execute_tool(
                    name=tool_name,
                    args=tool_args,
                    affaire_id=affaire_id,
                    db=db,
                )

                duration_tool = int((time.monotonic() - t_tool) * 1000)
                steps.append({
                    "tool": tool_name,
                    "args": tool_args,
                    "output": tool_output[:1000],  # tronqué pour le stockage
                    "duration_ms": duration_tool,
                })

                # Réinjecter le résultat dans les messages
                messages.append({
                    "role": "tool",
                    "tool_call_id": tc.id,
                    "content": tool_output,
                })

        else:
            # max_iterations atteint sans réponse finale
            final_answer = (
                "Limite d'itérations atteinte. Voici ce que j'ai trouvé jusqu'ici :\n"
                + (steps[-1]["output"] if steps else "Aucune information collectée.")
            )

        run.status = "completed"
        run.result = final_answer

    except Exception as exc:
        log.error("agent.run_failed", run_id=str(run.id), error=str(exc))
        run.status = "failed"
        run.result = f"Erreur lors de l'exécution : {exc}"

    finally:
        run.steps = steps
        run.iterations = len([s for s in steps]) // max(len(DEFINITIONS), 1) + 1
        run.duration_ms = int((time.monotonic() - t_start) * 1000)
        await db.commit()
        await db.refresh(run)

    log.info(
        "agent.run_complete",
        run_id=str(run.id),
        status=run.status,
        steps=len(steps),
        duration_ms=run.duration_ms,
    )
    return run
