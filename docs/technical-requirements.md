# Technical requirements

- [Technical requirements](#technical-requirements)
  - [Aim and the main problem to solve](#aim-and-the-main-problem-to-solve)
  - [Requirements](#requirements)

## Aim and the main problem to solve

Most weather services and apps show temperature as bare numbers. But it is not what most of us want to know. Obvious solution is "Feels like" temperature. It takes humidity, wind and many other measurements into an account and that is why it is much more informative. But unfortunately such temperature is not present in every service.

Another problem is necessity to manually check the weather, for example every morning before going to work.

The aim of this project is to provide actual weather information, send it to users using manual trigger or scheduled tasks, and use popular messenger such as Telegram instead of creating one more extra app or web service.

## Requirements

US - User Story

- [US-1] System should welcome user with message which contains short description of bot commands and some image. It should be displayed before starting any interaction with bot.
- [US-2] User is able to start interaction with bot. Starting message should contain description of bot commands and keyboard buttons with these commands.
- [US-3] User should be able to change settings. Location, schedule of sending periodic messages and language should be available for modification.
  - [US-4] User is able to change location (both persistently and temporary? Sometimes it's necessary to check weather in other locations only several times).
  - [US-5] User should be able to change language. Telegram's language is set by default.
  - [US-6] User should be able to change schedule of sending periodic messages.
- [US-7] System should store user data (only settings for now) in persistent storage. It is necessary to avoid data loss between expected and unexpected system restarts.
- [US-8] System should implement native Telegram bot menu with list of available commands and their short description.
- [US-9] System should provide required command for showing help information.
- [US-10] System should provide command for retrieving current weather conditions based on user settings.
- [US-11] System should provide command for retrieving today's weather conditions.
- [US-12] System should provide command for retrieving tomorrow's weather conditions.
- [US-13] System should provide command for week's weather conditions.
- [US-14] System should handle OpenWeatherMap API unavailability.
