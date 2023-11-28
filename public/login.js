const botaoLogin = document.querySelector("#login-button button")
const botaoDBA = document.querySelector("#enviar")

var token = 0

botaoLogin.addEventListener("click", async function (e) {
  const usuario = document.querySelector("#input-cpf input").value
  const senha = document.querySelector("#input-senha input").value
  const url = "http://127.0.0.1:8000/auth/token"
  const dadosJson = {
    usuario_id: usuario,
    tipo_usuario: "DBA",
    senha: senha,
  }

  try {
    const response = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(dadosJson),
    })

    if (!response.ok) {
      throw new Error(
        `Erro na requisição: ${response.status} - ${response.statusText}`
      )
    }

    const data = await response.json()
    console.log("Resposta:", data)

    guardarToken(data)
    abrirDBA()

    // Se necessário, faça algo com a resposta
  } catch (error) {
    console.error("Erro:", error)
  }
})

function guardarToken(data) {
  token = data["access_token"]
}

function abrirDBA() {
  window.location.href = "./DBA_page.html"
}

botaoDBA.addEventListener("click", async function (e) {
  const input = document.getElementsByClassName("textarea").value
  console.log(input)
  const url = "http://127.0.0.1:8000/dba/"
  const dadosJson = {
    sql: input,
  }

  const token =
    "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c3VhcmlvX2lkIjoiQURNSU4iLCJ0aXBvX3VzdWFyaW8iOiJEQkEiLCJleHAiOjE3MDM3MjE1MzR9.5L11PS2w4-2bqbh9nUb9pAeTEV2upqVtEtYwuoPxEHM"

  try {
    const response = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: token, // Adicionando o token ao cabeçalho
      },
      body: JSON.stringify(dadosJson),
    })

    if (!response.ok) {
      throw new Error(
        `Erro na requisição: ${response.status} - ${response.statusText}`
      )
    }

    const data = await response.json()
    console.log("Resposta:", data)

    guardarToken(data)
    abrirDBA()

    // Se necessário, faça algo com a resposta
  } catch (error) {
    console.error("Erro:", error)
  }
})
