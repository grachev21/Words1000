# Пользователь создает аккаунт:

- Срабатывает `settings/signal` который создает запись в настройках 
пользователя `settings/WordsSettings`: 


> [!NOTE]
> 
> Данные которые устанавливаются при 
> сробатывании сигнала --> 

```python
    number_words = models.IntegerField = 20
    number_repetitions = models.CharField = 2
    translation_list = models.BooleanField = True
    user = models.ForeignKey
> ```


- Срабатывает `users/signal` при регистрации или первичном входе в аккаунт, модель `users/WordsUser` заполняется 
списком слов в случайном порядке. 

> [!NOTE]
> Поля которые заполняются в `users/singal` -->

```python
    created_at = models.DateTimeField
    number_repetitions = models.IntegerField
    status = models.CharField
    user = models.ForeignKey
    core_words = models.ForeignKey
```



----



# Изменение пользовательских настроек:

- Класс представления `settings/view/SettingsPage` обновляет данные в `settings/models/WordsSettings`.


>[!bUg]
>

>[!WARNING]
>

>[!TIP]
>

>[!NOTE]
>




















































