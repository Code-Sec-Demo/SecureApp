document.addEventListener("DOMContentLoaded", () => {
    const welcome = document.getElementById("welcome");
    const results = document.getElementById("results");

    const name = localStorage.getItem("user_name");
    if (name) {
        welcome.innerHTML = "Hello, " + name + "!";
    }

    const form = document.getElementById("searchForm");
    if (form) {
        form.addEventListener("submit", (e) => {
            e.preventDefault();
            const q = document.getElementById("searchBox").value;

            fetch("/search?q=" + encodeURIComponent(q))
                .then(res => res.json())
                .then(data => {
                    results.innerHTML = "";
                    data.results.forEach(r => {
                        const div = document.createElement("div");
                        div.innerHTML = r.message;
                        results.appendChild(div);
                    });
                });
        });
    }
});
