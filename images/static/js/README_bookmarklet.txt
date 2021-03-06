// Это основной сценарий jQuery загрузчика. Он заботится об 
// использовании jQuery, если он уже загружен на текущий веб-сайт, 
// если нет он загружает его из сети CDN. Когда jQuery загружается, 
// она выполняет функцию bookmarklet(), которая будет содержать код 
// закладки. Мы также установили некоторые переменные в верхней 
// части файла:

// jquery_version : Версия jQuery для загрузки

// site_url and static_url : Базовый URL-адрес для нашего веб-сайта 
// и базовый URL-адрес для статических файлов

// min_width и min_height : Минимальная ширина и высота в пикселях 
// для изображений, которые наша кнопка-bookmarklet будет пытаться 
// найти на сайте


// load CSS

Этот код работает следующим образом:

Мы загрузили таблицу стилей bookmarklet.css, используя случайное 
число в качестве параметра, чтобы обойти кэширование файла в 
браузере.
Добавляем в <body> элемент <div>, который будет содержать 
изображения, найденные на текущем сайте.
Мы добавляем событие, которое удаляет наш HTML из документа, 
когда пользователь щелкает ссылку «закрыть» в нашем блоке HTML. 
Для поиска элемента HTML с ID close, который имеет родительский 
элемент с ID bookmarklet, используется селектор #bookmarklet 
#close. Селектор jQuery возвращает все элементы, найденные 
заданным селектором CSS. Список jQuery 
выборок можно найти в http://api.jquery.com/category/selectors/

// find images and display them

Этот код использует селектор img[src$="jpg"] для поиска всех 
элементов <img>, атрибут src совпадения оканчания jpg. 
Это означает, что мы найдем все JPG-изображения, отображаемые 
на текущем веб-сайте. Мы перейдем по результатам, используя 
метод jQuery each(). Мы добавляем контейнер <div class="images"> 
изображения с размером больше, чем тот, который задается с 
помощью переменных min_width и min_height.

Теперь контейнер HTML включает изображения, которые могут быть 
закладками. Мы хотим, чтобы пользователь нажимая на нужное 
изображение Добавлял его в закладки. 
Добавьте следующий код в нижнюю часть функции-bookmarklet():

// when an image is selected open URL with it

Этот код работает следующим образом:

Мы присоединяем событие click() к элементам связи изображений.
Когда пользователь щелкает на изображение, мы устанавливаем 
новую переменную с именем selected_image, которая содержит 
URL-адрес выбранного изображения.
Мы прячем закладку и открываем новое окно браузера с URL-адресом 
для закладки нового изображения на нашем сайте. Мы проходим 
<title> элемент веб-сайта и выбранный URL-адрес изображения в 
качестве параметров GET