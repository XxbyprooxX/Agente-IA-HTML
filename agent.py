import ollama
from skill_loader import load_all_skills
from project_writer import save_project_from_response

MODEL = "qwen2.5-coder:7b"
#MODEL = "qwen3:4b"

def build_system_prompt() -> str:
    skills = load_all_skills()

    return f"""
Eres un agente local especializado en generación de archivos HTML con CSS.

Debes usar las siguientes skills cargadas desde archivos Markdown:

{skills}
"""


def ask_agent(user_prompt: str) -> str:
    system_prompt = build_system_prompt()

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    return response["message"]["content"]


if __name__ == "__main__":
    print("Agente local HTML Y CSS con skills en Markdown")
    print("Escribe 'salir' para terminar.\n")

    while True:
        prompt = input("Solicitud: ")

        if prompt.lower() == "salir":
            break

        answer = ask_agent(prompt)
        print("\n--- RESPUESTA DEL AGENTE ---\n")
        print(answer)
        print("\n----------------------------------\n")
        project_dir = save_project_from_response(answer)

        print(f"\nProyecto generado en: {project_dir}\n")