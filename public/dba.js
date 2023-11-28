function dba(e) {
    const sql = document.querySelector(".textarea").value
    console.log(sql);
    const url = "http://127.0.0.1:8000/dba/";
    const dadosJson = {
        sql: "SELECT * FROM Agencia",
    };
    
    const token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c3VhcmlvX2lkIjoiMTI0NTk2MiIsInRpcG9fdXN1YXJpbyI6IkdFUkVOVEUiLCJleHAiOjE3MDM2MDM2ODR9.YNLpnTt2IHp4Z6n-QOtEPKMRWXm8vQQ7V_s6WrzPQSQ";
    
    fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": token, // Add this line to include the authorization token
        // You can add other headers if necessary
      },
      body: JSON.stringify(dadosJson),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(
            `Erro na requisição: ${response.status} - ${response.statusText}`
          );
        }
        return response.json();
      })
      .then((data) => {
        // Do something with the response data
        console.log("Resposta:", data);

      })
      .catch((error) => {
        // Handle errors during the request
        console.error("Erro:", error);
      });    
  }
  