function dba(e) {
    const sql = document.querySelector(".textarea").value
    console.log(sql);
    const url = "http://127.0.0.1:8000/dba/";
    const dadosJson = {
        sql: "SELECT * FROM Agencia",
    };
    
    const token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c3VhcmlvX2lkIjoiQURNSU4iLCJ0aXBvX3VzdWFyaW8iOiJEQkEiLCJleHAiOjE3MDM3OTA3Mzh9.o8K92_F8JEZ5jr_svwv0eEB7-FdqCw8lyjDSdcWBvXk";
    
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
  