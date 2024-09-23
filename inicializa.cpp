// Quando o meu sistema iniciar:
// Abre o ambiente virtual que permite executar a biblioteca que o main.py utiliza
// seleciona a task de uma lista de Tasks utilizando o arquivo linha que é um outfile do main.py
// Cria o arquivo task que vai ser usado pelo main.py
// executa o main.py

#include <cstdlib> // system()
#include <fstream> // Trabalhar com os arquivos
#include <string> // Permite trabalhar com strings
#include <iostream> // Para utilizar o cerr
using namespace std;

int lerLinhaDesejada() {
    ifstream entrada("linha.txt");  // Abrindo o arquivo

    if (!entrada.is_open()) {
    	entrada.close();
        return -1;  // Retorna um valor de erro
    }

    int linhaDesejada;
    entrada >> linhaDesejada;  // Lê o valor do arquivo

    entrada.close();
    return linhaDesejada;  // Retorna o valor lido
}

string selecionaTask(int linhaDesejada){ // Seleciona a task da lista de tasks
	ifstream entrada("listaTasks.txt");
	int contador = 0;
	string linha;

	if (!entrada.is_open()) {
		entrada.close();
        return "Erro ao abrir o arquivo"; // Retorna o erro
    }

    while(getline(entrada, linha)){ // Lê o arquivo linha por linha
    	contador++;
    	if(contador == linhaDesejada){// Retorna a task e sai da função
    		entrada.close();
    		return linha; 
    	}
    }

    entrada.close();
    return "Linha não encontrada (Erro no metodo selecionaTask)";  // Retorna o erro
}

int main(int argc, char const *argv[])
{
	//cadeia de comandos a ser executado pois meu sistema linux não me permite executar a biblioteca python que eu preciso fora de um ambiente virtual
	const char* comando = "bash -c 'cd && cd /home/maquina/Desktop/AmbienteVirtualPy && source myenv/bin/activate && cd && cd /home/maquina/Desktop/pastaTECH/ideias/medeTesks && python3 main.py'";
	ofstream saida;
	saida.open("task.txt");

	int linhaDesejada = lerLinhaDesejada(); // Descobre qual é a linha desejada

	if (linhaDesejada == -1)
	{
		cerr << "Erro ao abrir o arquivo (Função linhaDesejada).";
		exit(1);
	}

	string task = selecionaTask(linhaDesejada); // Extrai a proxima task

	if (task == "Erro ao abrir o arquivo") 
	{
        cerr << "Erro ao abrir o arquivo(Função selecionaTask)" << endl;  
        exit(1);// Exibe a mensagem de erro
    }

    saida << task;

    saida.close();

	system(comando); // Executa o comando

	return 0;
}
