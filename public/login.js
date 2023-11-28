var token

function imprimir(){
  console.log(sessionStorage.getItem("token"))
}
function login(e) {
  const usuario = document.querySelector("#input-cpf input").value
  const senha = document.querySelector("#input-senha input").value
  console.log(senha)
  const url = "http://127.0.0.1:8000/auth/token"
  const dadosJson = {
    usuario_id: usuario,
    tipo_usuario: "DBA",
    senha: senha,
  }

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      // Se necessário, adicione outros cabeçalhos aqui
    },
    body: JSON.stringify(dadosJson),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error(
          `Erro na requisição: ${response.status} - ${response.statusText}`
        )
      }
      return response.json()
    })
    .then((data) => {
      // Faça algo com os dados da resposta (data)
      console.log("Resposta:", data)
      guardarToken(data)
      abrirDBA()
    })
    .catch((error) => {
      // Trate os erros durante a requisição
      console.error("Erro:", error)
    })
}

function guardarToken(data) {
  token = data["access_token"]
  sessionStorage.setItem("token", token)
}

function abrirDBA() {
  window.location.href = "./DBA_page.html"
}
