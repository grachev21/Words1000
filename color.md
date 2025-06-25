Вот список **только названий** CSS-переменных (цветов), которые изменяются при смене темы в Bootstrap 5:

### Основные цвета:
```
--bs-body-color
--bs-body-bg
--bs-emphasis-color
--bs-secondary-color
--bs-secondary-bg
--bs-tertiary-bg
--bs-heading-color
--bs-link-color
--bs-link-hover-color
--bs-border-color
--bs-border-color-translucent
--bs-code-color
--bs-highlight-bg
```

### Семантические цвета:
```
--bs-primary
--bs-secondary
--bs-success
--bs-info
--bs-warning
--bs-danger
--bs-light
--bs-dark
```

### RGB-версии (для прозрачности):
```
--bs-primary-rgb
--bs-secondary-rgb
--bs-success-rgb
--bs-info-rgb
--bs-warning-rgb
--bs-danger-rgb
--bs-light-rgb
--bs-dark-rgb
--bs-body-color-rgb
--bs-body-bg-rgb
--bs-emphasis-color-rgb
--bs-secondary-color-rgb
--bs-secondary-bg-rgb
--bs-tertiary-bg-rgb
--bs-link-color-rgb
--bs-link-hover-color-rgb
```

Все эти переменные автоматически обновляются при изменении атрибута `data-bs-theme` между `light` и `dark`. Для кастомных стилей всегда используйте эти переменные вместо фиксированных цветов, чтобы обеспечить корректное переключение тем.