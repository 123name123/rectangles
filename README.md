<body>
<h1>Rectangles</h1>
<p>Это приложение на Python, которое получает координаты прямоугольников и располагает их в пространстве так, чтобы они
    не пересекались и находились как можно ближе друг к другу.</p>
<h1>Установка</h1>
<ol>
    <li>
        <p>Склонируйте репозиторий на свой компьютер</p>
        <pre>git clone https://github.com/123name123/rectangles_project.git</pre>
    </li>
    <li>
        <p>Перейдите в директорию проекта:</p>
        <pre>cd rectangles_project</pre>
    </li>
    <li>
        <p>Установите зависимости из файла <code>requirements.txt</code></p>
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
</ol>

<h1>Использование</h1>
<ol>
    <li>Запустите приложение:
        <pre><code>python src/main.py</code></pre>
    </li>
    <li>Введите координаты прямоугольников в следующем формате:
        <pre><code>x_min y_min x_max y_max</code></pre>
        <p><code>x_min</code> и <code>y_min</code> - координаты верхнего левого угла прямоугольника<br>
            <code>x_max</code> и <code>y_max</code> - координаты нижнего правого угла прямоугольника.</p>
    </li>
</ol>
<h1>Алгоритм</h1>
<ol>
    <li>Сдвигаем прямоугольники, чтобы левый нижний угол был в точке (0, 0)</li>
    <li>Находим максимальные рамки расположения прямоугольников</li>
    <li>Далее пытаемся максиммизировать площадь объединения прямоугольников повторяя следующие итерации:
        <ol>
            <li>Для каждого прямоугольника в наборе:
                <ul>
                    <li>Сгенерировать случайный вектор, определяющий перемещение прямоугольника внутри максимальных
                        рамок расположения
                    </li>
                    <li>Переместить прямоугольник в соответствии с вектором</li>
                </ul>
            </li>
            <li>Найти площадь объединения прямоугольников с помощью библиотеки <code>shapely</code></li>
        </ol>
    </li>
</ol>
