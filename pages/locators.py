from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "[name = 'j_username']")
    PASSWORD_FORM = (By.CSS_SELECTOR, "[name = 'j_password']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[type = button]")

class BasePageLocators:
    NORM_PRAV_MENU = (By.XPATH, "//*[@id='link2']")
    OPER_DATA_MENU = (By.XPATH, "//div[contains(text(), 'Оперативные данные')]")
    PLAN_GOZ_MENU = (By.XPATH, "//div[contains(text(), 'Планирование ГОЗ/ФЦП')]")
    REPORTS_MENU = (By.XPATH, "//*[@id='link5']")
    SEARCH_DOCS_MENU = (By.XPATH, "//div[contains(text(), 'Поиск документов')]")
    DIGITAL_DOCS_MENU = (By.XPATH, "//div[contains(text(), 'Электронные документы')]")
    ADMIN_MENU = (By.XPATH, "//div[contains(text(), 'Администрирование')]")

    EXIT_BUTTON = (By.CSS_SELECTOR, "div.welcome input")
    INFO_HELP_BUTTON = (By.XPATH, "//div[contains(@class, 'welcome')]/span[3]")
    SETTINGS_BUTTON = (By.XPATH, "//div[contains(@class, 'welcome')]/span[2]")

class SiteMapLocators:
    MAIN_MAP_LINK = (By.XPATH, "//div[contains(@class, 'site_map')]/a[contains(text(),'Главная')]")
    WORK_TABLE_MAP_LINK = (By.XPATH, "//ul/li/a[contains(text(),'Рабочий стол')]")

    NORMATIVE_REFERENCE_MAP_LINK = (By.XPATH, "//div[contains(@class, 'site_map')]//a[contains(text(),'Нормативно-справочная информация')]")
    NR_PROGRAM_MAP_LINK = (By.XPATH, "//div[contains(@class, 'site_map')]//a[contains(text(),'Программа/подпрограмма')]")
    NR_DOCS_MAP_LINK = (By.XPATH, "//div[contains(@class, 'site_map')]//a[contains(text(),'Нормативно-справочная информация и документы')]")
    NR_GOS_OBR_MAP_LINK = (By.XPATH, "//div[contains(@class, 'site_map')]//a[contains(text(),'ГосОборонЗаказ')]")
    NR_ORGANISATIONS_MAP_LINK = (By.XPATH, "//div[contains(@class, 'site_map')]//a[contains(text(),'Организации')]")

    OPERATIVE_DATA_MAP_LINK = (By.XPATH, "//div[contains(@class, 'site_map')]//a[contains(text(),'Оперативные данные')]")
    OD_ORDERS_MAP_LINK = (By.XPATH, "//div[contains(@class, 'site_map')]//a[contains(text(),'Размещение заказов')]")
    OD_NIOKR_MAP_LINK = (By.XPATH, "//div[contains(@class, 'site_map')]//a[contains(text(),'Каталог НИОКР')]")
    OD_PURCHASES_MAP_LINK = (By.XPATH, "//div[contains(@class, 'site_map')]//a[contains(text(),'Каталог закупок')]")
    OD_WORKS_MAP_LINK = (By.XPATH, "//div[contains(@class, 'site_map')]//a[contains(text(),'Список работ')]")
    OD_INTEGRAL_CONTROL_MAP_LINK = (By.XPATH, "//div[contains(@class, 'site_map')]//a[contains(text(),'Интегральный контроль')]")
    OD_NOTIFICATIONS_SETTING_MAP_LINK = (By.XPATH, "//div[contains(@class, 'site_map')]//a[contains(text(),'Настройка уведомлений')]")
    OD_CONTRACTS_MAP_LINK = (By.XPATH, "//div[contains(@class, 'site_map')]//a[contains(text(),'Сводная информация по контрактам')]")
    OD_EVENT_ANALYSIS_MAP_LINK = (By.XPATH, "//div[contains(@class, 'site_map')]//a[contains(text(),'Анализ выполнения мероприятий')]")
    OD_SUPPLY_MAP_LINK = (By.XPATH, "//div[contains(@class, 'site_map')]//a[contains(text(),'Поставки')]")
    OD_SUPPLY_PRODUCT_MAP_LINK = (By.XPATH, "//div[contains(@class, 'site_map')]//a[contains(text(),'Изделия')]")
    OD_SUPPLY_EXAMPLES_PRODUCT_MAP_LINK = (By.XPATH, "//div[contains(@class, 'site_map')]//a[contains(text(),'Экземпляры изделий')]")
    OD_SUPPLY_WORKS_MAP_LINK = (By.XPATH, "//div[contains(@class, 'site_map')]//a[contains(text(),'Работы по изделиям')]")
    OD_SUPPLY_SERVICE_MAP_LINK = (By.XPATH, "//div[contains(@class, 'site_map')]//a[contains(text(),'Обслуживание изделий')]")
    OD_REMAINING_PAYMENTS_MAP_LINK = (By.XPATH, "//div[contains(@class, 'site_map')]//a[contains(text(),'Остаток выплат')]")
    OD_CLAIM_MAP_LINK = (By.XPATH, "//div[contains(@class, 'site_map')]//a[contains(text(),'Претензии и исковые требования')]")

    PLANS_GOZ_FCP_MAP_LINK = (By.XPATH, "//div[contains(@class, 'site_map')]//a[contains(text(),'Планирование ГОЗ/ФЦП')]")
    PGF_CORRECTING_FCP_MAP_LINK = (By.XPATH, "//div[contains(@class, 'site_map')]//a[contains(text(),'Корректируемые ФЦП')]")
    PGF_PLANNING_GOZ_MAP_LINK = (By.XPATH, "//div[contains(@class, 'site_map')]//a[contains(text(),'Планируемые ГОЗ')]")
    PGF_PLAN_REPORT_FORMS_MAP_LINK = (By.XPATH, "//div[contains(@class, 'site_map')]//a[contains(text(),'Плановые отчетные формы')]")

    REPORT_FORMS_MAP_LINK = (By.XPATH, "//div[contains(@class, 'site_map')]//a[contains(text(),'Отчетные формы')]")
    DOC_SEARCH_MAP_LINK = (By.XPATH, "//div[contains(@class, 'site_map')]//a[contains(text(),'Поиск документов')]")
    DIGITAL_DOCS_MAP_LINK = (By.XPATH, "//div[contains(@class, 'site_map')]//a[contains(text(),'Электронные документы')]")

