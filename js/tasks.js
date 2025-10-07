// === Элементы ===
// находим все необходимые элементы на странице и сохраняем в переменные
const buttonTheme = document.getElementById("themeToggle");
const taskInput=document.getElementById("taskInput");
const taskList=document.getElementById("taskList");
const totalTasksSpan=document.getElementById("totalTasks");
const completedTasksSpan=document.getElementById("completedTasks");
const addTaskBtn = document.getElementById('addTaskBtn')

//Массив для хранения данных(задач)
let tasks =[];


function ToggleTheme(){
    taskInput.classList.toggle('darktheme');
    document.body.classList.toggle("dark-theme");

    if(document.body.classList.contains("dark-theme")){
        buttonTheme.textContent = "☀️ Светлая тема";
        localStorage.setItem("darkTheme", "enabled");
    }else{
        buttonTheme.textContent = "🌙 Темная тема";
        localStorage.setItem("darkTheme", "disabled");
    }
}

//===функции для работы с задачами===
//функция добавления новой задачи
function addTask(){
    //trim-убираем лишние проблемы в значении
    const tasktext = taskInput.value.trim();
    //проверка на пустое поле ввода
    if (tasktext == ""){
        alert("Пожайлуста введите задачу");
        return; //выход из функции(проверка выполнения функции)
    }
    //Создание обьекта задачи
    //обьект- это структурв,которая хранит данные в виде пар-ключ,значение
    const newTask={
        id: Date.now(),
        text: tasktext,
        completed: false
    }
    //добавление нашей задачи в список (массив) задач
    //push()-добавление элемента в конец списка (append in python)
    tasks.push(newTask);
    //очищаем поля ввода после внесения данных
    taskInput.value="";

    saveTasks();
    //обновляем список задач(отображение списка)
    renderTasks();
    //обновляем счетчики задач
    updateCounters();
} 

// Функция для выполнения задач
function toggleTaskCompletion(taskId){
    // Будем искать задачу в массиве по ID
    // find() - метод посика элемента в массиве 
    const task = tasks.find(task => task.id === taskId)

    // Если задача найдена 
    if(task){
        task.completed = !task.completed; // Преобразовать в противоположное значение 
        saveTasks();
        renderTasks();
        updateCounters();
    }
}

// Функция удаления задач
function deleteTask(taskId){
    // filter() - метод создания нового массива с элементами, которые прошли фильтрацию 
    // Оставляем только те задачи, которые прошли проверку (их id не равен удаляемому)
    tasks = tasks.filter(task => task.id !== taskId);

    saveTasks();
    renderTasks();
    updateCounters();
}

//  Обновление счетчика задач, при изменении задач (удалении, добавлении и т.д.)
function updateCounters(){
    // length - свойство, которое возвращает число элементов в массиве 
    const totalTasks = tasks.length;

    const completedTasks = tasks.filter(task => task.completed).length;

    // Обновим счетчиков в HTML
    totalTasksSpan.textContent = totalTasks;
    completedTasksSpan.textContent = completedTasks;        
}
//функция отображения (обновления) всего списка задач
function renderTasks(){
//очищение текущего списка
taskList.innerHTML='';
//перебираем все элементы в массиве
// forEach()-метод перебора каждого элемента мвссива
tasks.forEach(task => {
    //создание элемента списка
    //createElement()-метод создания нового HTML-элемента
    const taskItem = document.createElement("li");
    taskItem.className="task-item";
    //добавление класса если задача выполнена
    if(task.completed){
taskItem.classList.add("completed");
    }
    //создание HTML структурф для новой задачи
    taskItem.innerHTML=`
        <input type="checkbox" class="task-checkbox" ${task.completed ? 'checked' : ''}> 
        <span class="task-text">${task.text}</span>
        <button class="delete-btn">❌</button>
    `;

    // Обработчик событий для чекбокса и крестика
    const checkbox = taskItem.querySelector('.task-checkbox');
    const deleteBtn = taskItem.querySelector('.delete-btn');

    // Обработка нажатия на чекбокс
    checkbox.addEventListener('click', () =>{
        toggleTaskCompletion(task.id);
    });
    
    deleteBtn.addEventListener('click', () =>{
        deleteTask(task.id);
    });
    // Обработка нажатия по крестику
    
    //добавляем задачу в список HTML
    //appendChild()- метод добавления элемента в конце другого элемента
    taskList.appendChild(taskItem);
  });
}
//===обработчик событий===
buttonTheme.addEventListener("click", ToggleTheme);

addTaskBtn.addEventListener("click", addTask);
//===инициализация==
//проверка сохраненной темы
if(localStorage.getItem("darkTheme") === "enabled"){
    document.body.classList.add("dark-theme");
    taskInput.classList.toggle('darktheme');
    buttonTheme.textContent="☀️ Светлая тема";


}


// Загружаем задачи из localstorage при загрузке странице
function loadTasks(){
    const savedTasks = localStorage.getItem('tasks');
    if(savedTasks){
        tasks = JSON.parse(savedTasks); // Преобразование строк обратно в массив

        renderTasks();
        updateCounters();
    }
}
// Сохраняем задачи в localStorage
function saveTasks(){
    // JSON.stringify - преобразуем массив задач в строку (важно для сохранения)
    localStorage.setItem('tasks', JSON.stringify(tasks));
}

// // Обновляем функцию добавление задачи, чтобы она сохраняла задачу в локальном хранилище
// const originalAddTasks = addTask;
// addTask = function(){
//     originalAddTasks();
//     saveTasks();
// };
// Загружаем задачи при запуске страницы
loadTasks();