async function loadNews() {
    const res = await fetch('http://127.0.0.1:8000/noticias?limit=5');
    const news = await res.json();
    const container = document.getElementById('news-container');
    container.innerHTML = '';
    news.forEach(item => {
        const card = document.createElement('div');
        card.innerHTML = `<h3>${item.title}</h3>
                          <p>${item.summary}</p>
                          <a href="${item.link}" target="_blank">Leia mais</a><hr>`;
        container.appendChild(card);
    });
}

// Atualiza a cada minuto
loadNews();
setInterval(loadNews, 60000);