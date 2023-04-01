
function fillCardByIds(data) {
    document.getElementById("author-name").innerText = data.name;

    document.getElementById("author-email").innerText = data.email;
    document.getElementById("author-email").href = "mailto:"+data.email;

    document.getElementById("author-bio-name").innerText = data.name;
}
function fillCardByClass(data) {
    
    // Искать наши поля мы будем по одному уже внутри нашего элемента карточки cardElem, а для этого сначала
    let cardElem = document.getElementById("author-card-to-fill-by-class"); // находим в документе элемент нашей карточки по id

    // Вообще говоря элементов с одинаковым классом может быть несколько, поэтому метод .getElementsByClassName() возвращает массив.
    // К счастью мы знаем что внутри карточки у нас всего один элемент каждого класса, поэтому смело берём его по индексу [0]
    let nameElem = cardElem.getElementsByClassName("author-name-cls")[0];
    nameElem.innerText = data.name;
    
    let emailElem = cardElem.getElementsByClassName("author-email-cls")[0];
    emailElem.innerText = data.email;
    emailElem.href = "mailto:"+data.email;
    
    let nameInBioElem = cardElem.getElementsByClassName("author-bio-name-cls")[0];
    nameInBioElem.innerText = data.name;
}

// выполнить действия после загрузки страницы
window.onload = function () {
    /* 
        В данном примере мы предпологаем, что бэкенд ещё к работе не готов, но мы уже договорились с
        участником команды, который отвечает за его разработку, о формате данных, поэтому можем его
        не ждать, а пока подставить данные вручную и делать свою часть.
        Куски же кода, отвечающие за fetch пока закомментированы

        Непосредственно по работе запросов fetch() см. пример 2 или по адресу:
        https://learn.javascript.ru/fetch
    */

    //fetch('http://127.0.0.1:8000/api/author/1', {mode: 'no-cors'})
    //    .then(response => response.json())
    //    .then(author => {
            //примерно здесь начинается обработка пришедших данных, сюда и делаем подстановку:
            let json = {
                "author": {
                    "name": "Илья Попутников",
                    "email": "poputnikoviv@yandex.ru"
                }
            }
            fillCardByIds(json.author);
            fillCardByClass(json.author);
            
    //    });
};