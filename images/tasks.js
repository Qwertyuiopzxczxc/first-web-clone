// === ПЕРЕМЕННЫЕ ===
// Находим все необходимые элементы на странице и сохраняем в переменные
const buttonTheme = document.getElementById('themeToggle');
const taskInput = document.getElementById('taskInput');
const addTaskBtn = document.getElementById('addTaskBtn');
const taskList = document.getElementById('taskList');
const totalTasksSpan = document.getElementById('totalTasks');
const completedTasksSpan = document.getElementById('completedTasks');

// Массив для хранения данных (задач)
let tasks = [];

function toggletheme(){
    // body - наш тэг из html файла
    // classList - получает весь список классов у элемента 
    // toggle - переключает класс (если класса нет - добавляет его, и удаляет если он есть)
    document.body.classList.toggle('dark-theme');

    // contains() - проверяет существование класса у элемента
    if(document.body.classList.contains('dark-theme')){
        // Используем переменную в которой хранится кнопка
        // button - это наша переменная, в которой хранится кнопка
        // textContent - это изменить содеримое текста тэга
        button.textContent = '☀️ Светлая тема';
        // Локальное хранение состояния темы (чтобы сохранить тему после перезагрузки)
        localStorage.setItem('darkTheme', 'enabled');
    }else{
        button.textContent = '🌙 Темная тема';
localStorage.setItem('darkTheme', 'disabled');
    }
}

// === ФУНКЦИИ ДЛЯ РАБОТЫ С ЗАДАЧАМИ ===

// Функция добавления новой задачи
function addTask(){
    // trim - убирает лишние пробелы в значении
    const taskText = taskInput.ariaValueMax.trim();

    // Проверка на пустое поле ввода
    if (taskText == '') {
        alert('Пожалуйста введите задачу!');
        return; // Выход из функции
    }

    // Создание объекта задачи
    // Объекты - это структура, которая хранит данные в виде пар - ключ, значение
    const newTask = {
        id: Date.now(),
        text: taskText,
        completed: false
    }

    // Добавление нашей задачи в список (массив) задач
    // push() - добавления элемента в конец списка (append в python)
    tasks.push(newTask);

    // Очищаем поля ввода после внесения данных
    taskInput.value = '';
    
    // Обновляем список задач (отображеие списка)
    renderTasks();

    // Обновляем счетчики задач
    updateCounters();    
}
// Функция отображения (обновления) всего списка задач
function renderTasks(){
    // Очищение текущего списка
    taskList.innerHTML = '';

    // Перебираем все элементы в массиве
    // forEach() - метод перебора каждого элемента массива
    tasks.forEach(task => {
        // Создание элемента списка
        // CreateElement() - метод создания нового HTML-элемента
        const taskItem = document.createElement("li");
        taskItem.className = "task-item";

        // Добавление класса если задача выполнена 
        if(task.completed){
            taskItem.classList.add("completed");
        }
        
        // Создание HTML структуры для новой задачи
        taskItem.innerHTML = `
            <span class="task-text">${task.text}</span>
        `;

        // Добавляем задачу в список HTML
        // appendChild() - метод добавления элемента в конец другого элемента
        taskList.appendChild(taskItem);
    });
}


// === ОБРАБОТЧИКИ СОБЫТИЙ ===
buttonTheme.addEventListener('click', toggletheme);
addTaskBtn.addEventListener('click', addTask);

// === ИНИЦИАЛИЗАЦИЯ ===
// Проверка сохраненной темы
if(localStorage.getItem('darkTheme') === 'enabled'){
    document.body.classList.add('dark-theme');
    buttonTheme.textContent = '☀️ Светлая тема';
}