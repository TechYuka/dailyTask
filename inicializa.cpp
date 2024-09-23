// gnome-session-properties  // Abre o app preferencia dos aplicativos inicias de sessão no ubuntu
// Esse programa cria um exe que dando executado inicializa o ambiente virtual presente na mesma pasta e dps o app
#include <cstdlib>

int main(int argc, char const *argv[])
{
	const char* comando = "bash -c ' source myenv/bin/activate && python3 main.py'";

	system(comando);

	return 0;
}
