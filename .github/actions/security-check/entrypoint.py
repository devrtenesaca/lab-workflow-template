import os
import sys
def run():
# 1. Obtener el input desde las variables de entorno (GitHub las pasa así)
    dockerfile_path = os.getenv("INPUT_DOCKERFILE-PATH")
    
    if not os.path.exists(dockerfile_path):
        print(f"❌ Error: No se encontró el archivo {dockerfile_path}")
        sys.exit(1)

    with open(dockerfile_path, 'r') as f:
        content = f.read()
        if "latest" in content.lower():
            print("⚠️ ADVERTENCIA: Se detectó el uso de 'latest'. Usa versiones específicas.")
            # Podríamos usar sys.exit(1) para fallar, pero solo daremos un aviso
            #sys.exit(1)
        else:
            print("✅ Todo bien: No se detectó el tag 'latest'.")

    # 2. Enviar un output (Escribir en el archivo de salida de GitHub)
    with open(os.getenv('GITHUB_OUTPUT'), 'a') as fh:
        print(f"status=finalizado", file=fh)

if __name__ == "__main__":
    run()