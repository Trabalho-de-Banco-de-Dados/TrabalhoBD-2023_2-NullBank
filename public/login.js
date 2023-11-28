const botaoLogin = document.querySelector("#login-button button")
const usuario = document.querySelector("#input-cpf input").value
const senha = document.querySelector("#input-senha input").value

botaoLogin.addEventListener("click", function (e) {
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
    })
    .catch((error) => {
      // Trate os erros durante a requisição
      console.error("Erro:", error)
    })
})
