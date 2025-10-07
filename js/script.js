// document это объект, который предоставляет всю нашу HTML страницу
const button = document.getElementById('themetoggle');
const logo = document.getElementById('logotheme');

function toggletheme(){
    // body - наш тэг из html файла
    // classList - получает весь список классов у элемента 
    // toggle - переключает класс (если класса нет - добавляет его, и удаляет если он есть)
    document.body.classList.toggle('dark-theme');
    logo.classList.toggle('darktheme');

    // contains() - проверяет существование класса у элемента
    if(document.body.classList.contains('dark-theme')){
        // Используем переменную в которой хранится кнопка
        // button - это наша переменная, в которой хранится кнопка
        // textContent - это изменить содеримое текста тэга
        button.textContent = '☀️ Светлая тема';
    }else{
        button.textContent = '🌙 Темная тема';
    }
}

// Добавление обработчика события (нажатие на кнопку)
// addEventListener() - "слушает" события на элементе
// 'click' - тип события (клик мышкой)
// toggletheme - выполнить функцию, при нажатии (клике)
button.addEventListener('click', toggletheme);
