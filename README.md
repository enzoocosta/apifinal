# api-address-

rotas e comandos: 

*** mostrar todos enderecos - get =( http://127.0.0.1:5000/address ) - no navegador 

*** deletar endereco - delete =( curl -X DELETE http://127.0.0.1:5000/address/2 ) - o numero 2 é o id que voce quer apagar, ou seja, pode ser qualquer outro numero no lugar do 2, voce usa ele no cmd do vscode

*** adicionar/criar endereco - post =( curl -X POST -H "Content-Type: application/json" -d "{\"street\":\"jair garcia\",\"city\":\"itaqua\",\"state\":\"sao paulo\",\"postal_code\":\"12345\"}" http://127.0.0.1:5000/address ) - voce usa isso no cmd do vscode, os valores voce escolhe manualmente, essa barra invertida, pode dar errado em outras maquinas, atenção 

*** atualizar endereco - put =( curl -X PUT -H "Content-Type: application/json" -d "{\"street\":\"456 Elm St\",\"city\":\"New City\",\"state\":\"New State\",\"postal_code\":\"54321\"}" http://127.0.0.1:5000/address/1 ) - usado no terminal do vscode, na url o 1 no final é o id que voce quer atualizar, pode ser qualquer id, no caso agora foi o 1 

*** buscar endereço pelo id - get =( curl http://127.0.0.1:5000/address/from/3 ) - usado no terminal, o id procurado sera substituido pelo 2 
