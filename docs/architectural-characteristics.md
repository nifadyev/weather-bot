# Architectural characteristics

Most characteristics are aimed to ease project's development and maintenance. It doesn't clear now if project will be used by anyone or not. That's why priority is given to technical characteristics.

- [Architectural characteristics](#architectural-characteristics)
  - [Modifiability](#modifiability)
  - [Maintainability](#maintainability)
  - [Testability](#testability)
  - [Simplicity](#simplicity)
  - [Usability](#usability)

## Modifiability

The cost and risks of making changes. Important for most Open Source projects.

- System components should be low coupled (how low?)

## Maintainability

The complexity of recovering system after failures or changing other characteristics.

- System should write extensive logs to quickly (how quickly?) find the cause of error
- System should be able to quickly (how quickly?) recover by rolling back to previous working state
- System should be able to handle failures of external systems such as OpenWeatherMap API

## Testability

Ease and fullness of testing.

- Test coverage should be at least 70%. Actual value depends on system implementation
- Every change in system implementation should be tested if possible

## Simplicity

System's clarity for everyone who interact with it. Important for most Open Source projects.

- System should contain relevant documentation
- Every change in system implementation should be well documented
- Routine processes should be automated if possible

## Usability

Ease of use and effectiveness of interaction with system.

- Total time from executing command (from menu, pushing button) to returning message should be less than N seconds (probably 3 seconds)
- System should always return message. Even in case of internal error
- System should respect user settings
