# Содержание

- [Содержание](#содержание)
- [Цель проекта (основная проблема, которую решает проект)](#цель-проекта-основная-проблема-которую-решает-проект)
- [Требования](#требования)

# Цель проекта (основная проблема, которую решает проект)

Показатели температуры в большинстве погодных приложений и сервисов не отражают реальной погоды. Температура "по ощущениям" гораздо информативнее, но имеется не в каждом сервисе.
Вторая проблема - необходимость вручную проверять погоду, например с утра перед работой
Цель - создать сервис в удобном популярном мессенджере (Telegram), который будет присылать по заданным пользователям периодам и вручную полезную информацию о погоде.

# Требования

US - User Story

- [US-1] Система должна отображать сообщение с краткой информацией до запуска бота. Сообщение должно содержать текущие возможности бота и SVG изображение
- [US-2] Пользователь может запустить бота. Стартовое сообщение должно содержать описание возможностей и кнопки с основными командами
- [US-3] Пользователь должен иметь возможность модифицировать настройки. Настройки включают в себя локацию, периодические сообщения, язык
  - [US-4] Пользователь может задать локацию для получения погоды на основе данных из Telegram
  - [US-5] Пользователь может изменить язык бота. По умолчанию выбран язык Telegram
  - [US-6] Пользователь может изменить периодичность отправки сообщений
- [US-7] Система должна сохранять пользовательские настройки между вынужденными и непредвиденными перезапусками в БД
- [US-8] Система должна содержать нативное меню Telegram ботов со списком доступных на данный момент команд и их описанием
- [US-9] Система должна реализовать обязательную команду для старта бота. Эта же команда отвечает за перезапуск
- [US-10] Система должна реализовать обязательную команду для вывода справочной информации
- [US-11] Система должна реализовать команду для получения текущей погоды с учетом заданных настроек пользователя
- [US-12] Система должна реализовать команду для получения погоды на сегодня
- [US-13] Система должна реализовать команду для получения погоды на завтра
- [US-14] Система должна реализовать команду для получения погоды на 7 дней
- [US-15] Система должна реализовать команду для создания периодической задачи
- [US-16] Система должна обрабатывать недоступность OpenWeatherMap API