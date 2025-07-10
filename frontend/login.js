document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("loginForm");

    if (!form) return;

    form.addEventListener("submit", (e) => {
        e.preventDefault();

        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        fetch("/api/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ username, password })
        }).then(res => res.json())
          .then(data => {
              if (data.token) {
                  localStorage.setItem("token", data.token);
                  window.location.href = "/dashboard.html";
              } else {
                  alert("Login failed");
              }
          }).catch(err => {
              console.error("Login error:", err);
          });
    });
});
