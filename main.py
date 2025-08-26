from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screenmanager import MDScreenManager
from kivy.uix.screenmanager import NoTransition,ScreenManager
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivymd.uix.behaviors import MagicBehavior,HoverBehavior
from kivymd.uix.button import MDRaisedButton,MDIconButton
from kivymd.uix.tooltip import MDTooltip

from time import strftime
import sqlite3
from kivymd.toast import toast
from kivymd.uix.datatables import MDDataTable
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel

#Window.size = [340,620]

Builder.load_file("Pages/Page1.kv")
Builder.load_file("Pages/Page2.kv")
Builder.load_file("Pages/Page3.kv")
Builder.load_file("Pages/Page4.kv")

class But(MDRaisedButton , MagicBehavior,HoverBehavior):
    def on_enter(self):
        self.size_hint = .3,.1
        self.Font = self.font_size
        self.font_size = 20
    
    def on_leave(self):
        self.size_hint= .15,.05
        self.font_size = self.Font

class Icon(MDIconButton,HoverBehavior):
    def __init__(self, text="", **kwargs):
        super().__init__(**kwargs)
        self.text = text
        # Menu qui s'affiche au survol
        self.tooltip_menu = MDDropdownMenu(
            width=dp(50),
            )
        
    def on_enter(self):
        self.tooltip_menu.caller = self
        self.tooltip_menu.items=[{"text": self.text}]
        self.tooltip_menu.open()
        
    def on_leave(self):
        self.tooltip_menu.dismiss()


class Page1(MDScreen):
    pass

class Page2(MDScreen):
    pass

class Page3(MDScreen):
    pass

class Page4(MDScreen):
    pass

class BCC(MDApp):
    Langue = {
    "fr": {
        "Page1": {
            "1": "[b]LOGICIEL DE CONTRÔLE DU BCC[/b]",
            "2": "[b]CEET-DRM-BCC[/b]",
            "3": "[b]Aller[/b]"
        },
        "Page2": {
            "1": "[b]BIENVENUE \n VEUILLEZ SÉLECTIONNER VOTRE ACTION[/b]",
            "2": "[b]HISTOIRE[/b]",
            "3": "[b]AJOUTER[/b]",
            "4": "Aide",
            "5": "Changer de fonds (Nuit/Jour)",
            "6": "Accueil",
            "7": "Saisir information",
            "8": "Choix",
            "9": "Histoire",
            "10": "Couleur"
        },
        "Page3": {
            "1": "[b]VEUILLEZ REMPLIR CETTE PAGE[/b]",
            "2": "Date",
            "3": "Operateur",
            "4": "Ouverture ou fermerture ou DD",
            "5": "Operation",
            "6": "Mension(succes ou Ic)",
            "7": "Si il n'y a pas on met rien",
            "8": "[b]Valider[/b]"
        }
    },
    "en": {
        "Page1": {
            "1": "[b]BCC CONTROL SOFTWARE[/b]",
            "2": "[b]CEET-DRM-BCC[/b]",
            "3": "[b]Go[/b]"
        },
        "Page2": {
            "1": "[b]WELCOME \n PLEASE SELECT YOUR ACTION[/b]",
            "2": "[b]HISTORY[/b]",
            "3": "[b]ADD[/b]",
            "4": "Help",
            "5": "Switch theme (Light/Dark)",
            "6": "Home",
            "7": "Enter information",
            "8": "Choose",
            "9": "History",
            "10": "Color"
        },
        "Page3": {
            "1": "[b]PLEASE FILL OUT THIS PAGE[/b]",
            "2": "Date",
            "3": "Operator",
            "4": "Opening or closing or DD",
            "5": "Operation",
            "6": "Mention(success or Ic)",
            "7": "If there is nothing, leave empty",
            "8": "[b]Validate[/b]"
        }
    },
    "es": {
        "Page1": {
            "1": "[b]SOFTWARE DE CONTROL BCC[/b]",
            "2": "[b]CEET-DRM-BCC[/b]",
            "3": "[b]Ir[/b]"
        },
        "Page2": {
            "1": "[b]BIENVENIDO \n POR FAVOR SELECCIONE SU ACCIÓN[/b]",
            "2": "[b]HISTORIAL[/b]",
            "3": "[b]AÑADIR[/b]",
            "4": "Ayuda",
            "5": "Cambiar tema (Claro/Oscuro)",
            "6": "Inicio",
            "7": "Ingresar información",
            "8": "Elegir",
            "9": "Historial",
            "10": "Color"
        },
        "Page3": {
            "1": "[b]POR FAVOR COMPLETE ESTA PÁGINA[/b]",
            "2": "Fecha",
            "3": "Operador",
            "4": "Apertura o cierre o DD",
            "5": "Operación",
            "6": "Mención(éxito o Ic)",
            "7": "Si no hay nada, dejarlo vacío",
            "8": "[b]Validar[/b]"
        }
    },
    "de": {
        "Page1": {
            "1": "[b]BCC STEUERUNGSSOFTWARE[/b]",
            "2": "[b]CEET-DRM-BCC[/b]",
            "3": "[b]Gehen[/b]"
        },
        "Page2": {
            "1": "[b]WILLKOMMEN \n BITTE WÄHLEN SIE IHRE AKTION[/b]",
            "2": "[b]VERLAUF[/b]",
            "3": "[b]HINZUFÜGEN[/b]",
            "4": "Hilfe",
            "5": "Thema wechseln (Hell/Dunkel)",
            "6": "Startseite",
            "7": "Informationen eingeben",
            "8": "Auswählen",
            "9": "Verlauf",
            "10": "Farbe"
        },
        "Page3": {
            "1": "[b]BITTE FÜLLEN SIE DIESE SEITE AUS[/b]",
            "2": "Datum",
            "3": "Bediener",
            "4": "Öffnung oder Schließung oder DD",
            "5": "Betrieb",
            "6": "Erwähnung(Erfolg oder Ic)",
            "7": "Wenn nichts vorhanden ist, leer lassen",
            "8": "[b]Bestätigen[/b]"
        }
    },
    "zh": {  # Chinois simplifié
        "Page1": {
            "1": "[b]BCC控制软件[/b]",
            "2": "[b]CEET-DRM-BCC[/b]",
            "3": "[b]前往[/b]"
        },
        "Page2": {
            "1": "[b]欢迎 \n 请选择您的操作[/b]",
            "2": "[b]历史[/b]",
            "3": "[b]添加[/b]",
            "4": "帮助",
            "5": "切换主题（亮/暗）",
            "6": "主页",
            "7": "输入信息",
            "8": "选择",
            "9": "历史",
            "10": "颜色"
        },
        "Page3": {
            "1": "[b]请填写此页面[/b]",
            "2": "日期",
            "3": "操作员",
            "4": "开启或关闭或DD",
            "5": "操作",
            "6": "提及（成功或Ic）",
            "7": "如果没有内容，留空",
            "8": "[b]验证[/b]"
        }
    },
    "zh-tw": {  #// Chinois traditionnel
        "Page1": {
            "1": "[b]BCC控制軟體[/b]",
            "2": "[b]CEET-DRM-BCC[/b]",
            "3": "[b]前往[/b]"
        },
        "Page2": {
            "1": "[b]歡迎 \n 請選擇您的操作[/b]",
            "2": "[b]歷史[/b]",
            "3": "[b]添加[/b]",
            "4": "幫助",
            "5": "切換主題（亮/暗）",
            "6": "首頁",
            "7": "輸入資訊",
            "8": "選擇",
            "9": "歷史",
            "10": "顏色"
        },
        "Page3": {
            "1": "[b]請填寫此頁面[/b]",
            "2": "日期",
            "3": "操作員",
            "4": "開啟或關閉或DD",
            "5": "操作",
            "6": "提及（成功或Ic）",
            "7": "如果沒有內容，留空",
            "8": "[b]驗證[/b]"
        }
    },
    "ja": {  #// Japonais
        "Page1": {
            "1": "[b]BCC制御ソフトウェア[/b]",
            "2": "[b]CEET-DRM-BCC[/b]",
            "3": "[b]移動[/b]"
        },
        "Page2": {
            "1": "[b]ようこそ \n アクションを選択してください[/b]",
            "2": "[b]履歴[/b]",
            "3": "[b]追加[/b]",
            "4": "ヘルプ",
            "5": "テーマの切り替え（ライト/ダーク）",
            "6": "ホーム",
            "7": "情報を入力",
            "8": "選択",
            "9": "履歴",
            "10": "色"
        },
        "Page3": {
            "1": "[b]このページに記入してください[/b]",
            "2": "日付",
            "3": "オペレーター",
            "4": "開始または終了またはDD",
            "5": "操作",
            "6": "言及（成功またはIc）",
            "7": "何もない場合は空のままにする",
            "8": "[b]検証[/b]"
        }
    },
    "ko": {  #// Coréen
        "Page1": {
            "1": "[b]BCC 제어 소프트웨어[/b]",
            "2": "[b]CEET-DRM-BCC[/b]",
            "3": "[b]이동[/b]"
        },
        "Page2": {
            "1": "[b]환영합니다 \n 작업을 선택하세요[/b]",
            "2": "[b]기록[/b]",
            "3": "[b]추가[/b]",
            "4": "도움말",
            "5": "테마 전환 (밝음/어두움)",
            "6": "홈",
            "7": "정보 입력",
            "8": "선택",
            "9": "기록",
            "10": "색상"
        },
        "Page3": {
            "1": "[b]이 페이지를 작성해주세요[/b]",
            "2": "날짜",
            "3": "운영자",
            "4": "열기 또는 닫기 또는 DD",
            "5": "작업",
            "6": "언급(성공 또는 Ic)",
            "7": "없으면 비워두세요",
            "8": "[b]확인[/b]"
        }
    },
    "ar": {  #// Arabe
        "Page1": {
            "1": "[b]برنامج التحكم في BCC[/b]",
            "2": "[b]CEET-DRM-BCC[/b]",
            "3": "[b]انتقال[/b]"
        },
        "Page2": {
            "1": "[b]مرحباً \n يرجى اختيار إجراءك[/b]",
            "2": "[b]التاريخ[/b]",
            "3": "[b]إضافة[/b]",
            "4": "مساعدة",
            "5": "تغيير الثيم (فاتح/داكن)",
            "6": "الصفحة الرئيسية",
            "7": "إدخال المعلومات",
            "8": "اختيار",
            "9": "تاريخ",
            "10": "لون"
        },
        "Page3": {
            "1": "[b]يرجى ملء هذه الصفحة[/b]",
            "2": "التاريخ",
            "3": "المشغل",
            "4": "فتح أو إغلاق أو DD",
            "5": "العملية",
            "6": "الذكر(نجاح أو Ic)",
            "7": "إذا لم يكن هناك شيء، اتركه فارغاً",
            "8": "[b]التحقق[/b]"
        }
    },
    "ru": {  #// Russe
        "Page1": {
            "1": "[b]ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ УПРАВЛЕНИЯ BCC[/b]",
            "2": "[b]CEET-DRM-BCC[/b]",
            "3": "[b]Перейти[/b]"
        },
        "Page2": {
            "1": "[b]ДОБРО ПОЖАЛОВАТЬ \n ПОЖАЛУЙСТА, ВЫБЕРИТЕ ДЕЙСТВИЕ[/b]",
            "2": "[b]ИСТОРИЯ[/b]",
            "3": "[b]ДОБАВИТЬ[/b]",
            "4": "Помощь",
            "5": "Сменить тему (Светлая/Тёмная)",
            "6": "Главная",
            "7": "Ввести информацию",
            "8": "Выбрать",
            "9": "История",
            "10": "Цвет"
        },
        "Page3": {
            "1": "[b]ПОЖАЛУЙСТА, ЗАПОЛНИТЕ ЭТУ СТРАНИЦУ[/b]",
            "2": "Дата",
            "3": "Оператор",
            "4": "Открытие или закрытие или DD",
            "5": "Операция",
            "6": "Упоминание(успех или Ic)",
            "7": "Если ничего нет, оставить пустым",
            "8": "[b]Проверить[/b]"
        }
    },
    "pt": {  #// Portugais
        "Page1": {
            "1": "[b]SOFTWARE DE CONTROLE BCC[/b]",
            "2": "[b]CEET-DRM-BCC[/b]",
            "3": "[b]Ir[/b]"
        },
        "Page2": {
            "1": "[b]BEM-VINDO \n POR FAVOR SELECIONE SUA AÇÃO[/b]",
            "2": "[b]HISTÓRICO[/b]",
            "3": "[b]ADICIONAR[/b]",
            "4": "Ajuda",
            "5": "Mudar tema (Claro/Escuro)",
            "6": "Início",
            "7": "Inserir informação",
            "8": "Escolher",
            "9": "Histórico",
            "10": "Cor"
        },
        "Page3": {
            "1": "[b]POR FAVOR PREENCHA ESTA PÁGINA[/b]",
            "2": "Data",
            "3": "Operador",
            "4": "Abertura ou fechamento ou DD",
            "5": "Operação",
            "6": "Menção(sucesso ou Ic)",
            "7": "Se não houver nada, deixar vazio",
            "8": "[b]Validar[/b]"
        }
    },
    "it": {  #// Italien
        "Page1": {
            "1": "[b]SOFTWARE DI CONTROLLO BCC[/b]",
            "2": "[b]CEET-DRM-BCC[/b]",
            "3": "[b]Vai[/b]"
        },
        "Page2": {
            "1": "[b]BENVENUTO \n PER FAVORE SELEZIONA LA TUA AZIONE[/b]",
            "2": "[b]CRONOLOGIA[/b]",
            "3": "[b]AGGIUNGI[/b]",
            "4": "Aiuto",
            "5": "Cambia tema (Chiaro/Scuro)",
            "6": "Home",
            "7": "Inserire informazioni",
            "8": "Scegliere",
            "9": "Cronologia",
            "10": "Colore"
        },
        "Page3": {
            "1": "[b]PER FAVORE COMPILA QUESTA PAGINA[/b]",
            "2": "Data",
            "3": "Operatore",
            "4": "Apertura o chiusura o DD",
            "5": "Operazione",
            "6": "Menzione(successo o Ic)",
            "7": "Se non c'è niente, lasciare vuoto",
            "8": "[b]Convalidare[/b]"
        }
    }
}
    def __init__(self):
        super().__init__()
        self.Current_lang = "fr"

    def on_start(self):
        self.con = sqlite3.connect("base.db")
        cur = self.con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS BCC (id INTEGER PRIMARY KEY AUTOINCREMENT, Date TEXT, Operator TEXT, O_F_DD TEXT, Operation TEXT, Mension TEXT)")
        self.con.commit()
        self.DATE = strftime("%D")#Pour la date plus tart dans Page4
        self.PAGE4_Liste = []
        

        """Configuration au démarrage de l'app"""
        from kivy.core.window import Window
        from kivy.utils import platform
        
        if platform in ('android', 'ios'):
            # Configuration mobile
            Window.softinput_mode = 'below_target'
            
        # Lier l'événement de changement de taille (clavier)
        Window.bind(on_resize=self.on_window_resize)

        self.Verifi_moi_les_pages()

    def on_window_resize(self, window, width, height):
        """Appelé quand la fenêtre change de taille (clavier apparaît/disparaît)"""
        # Optionnel: ajuster le scroll automatiquement
        pass
        
    def on_close(self):
        self.con.close()
        
    def build(self):
        self.cr = ScreenManager()
        Liste = [Page1,Page2,Page3,Page4]
        for elmt in Liste:
            self.cr.add_widget(elmt())
        self.cr.transition = NoTransition()
        
        return self.cr
    
    def page1(self):
        Element = self.Langue.get(self.Current_lang).get("Page1")
        Pge = self.cr.current_screen.ids

        Liste = [Pge.Page1_1,Pge.Page1_2,Pge.Page1_3]

        for elmt,elmt2 in zip(Liste,Element.keys()):
            elmt.text = Element.get(elmt2)
    
    def Verifi_moi_les_pages(self):
        dic = {"Page1":self.page1 , "Page2":self.page2 , "Page3":self.page3,"Page4":self.page4}


        dic.get(self.cr.current)()

        Clock.schedule_once(lambda dt : self.Verifi_moi_les_pages(),.5)
    
    def Changer_font1(self,instance):
        self.theme_cls.theme_style = "Dark" if self.theme_cls.theme_style == 'Light' else "Light"
    
    def Changer_font2(self,instance):
        Liste = ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
        items = []
        for elmt in Liste:
            Add = {
                "text":elmt,
                "on_release":lambda x = elmt : self.COLOR(x)
            }
            items.append(Add)
        
        self.COLOR2 = MDDropdownMenu(
            caller = instance,
            items = items,
            width_mult = 3,
        )

        self.COLOR2.open()
    
    def COLOR(self,x):
        self.theme_cls.primary_palette = x
        self.COLOR2.dismiss()

    def page3(self):
        Element = self.Langue.get(self.Current_lang).get("Page3")
        Pge = self.cr.current_screen.ids


        Liste1 = [Pge.Page2_7,Pge.Page2_9,Pge.Page2_8,Pge.Page2_10,Pge.Page2_11]
        for elmt in Liste1:
            elmt.theme_text_color = "Custom"
            if Liste1.index(elmt) == 2:
                elmt.icon_color = [1,1,1,1]
            else:
                elmt.icon_color = [0,0,0,1]

        Liste = [Pge.Page3_1]
        Liste2 = [Pge.Page3_2,Pge.Page3_3,Pge.Page3_4,Pge.Page3_5,Pge.Page3_6,Pge.Page3_6]
        Liste3 = [Pge.Page3_7]
        Pge.Page2_4.text = self.Current_lang
        Val = None
        for elmt,elmt2 in zip(Liste+Liste2+Liste3,Element.keys()):
            if Val == elmt:
                elmt.helper_text = Element.get(elmt2)
            elif  elmt not in Liste+Liste3:
                elmt.hint_text = Element.get(elmt2)
            else:
                elmt.text = Element.get(elmt2)
            Val = elmt
            
        
        Date = strftime("%D")
        Pge.Page3_2.text = Date
        Pge.Page3_2.readonly = True
        Pge.Page3_4.readonly = True

        #Essay de fair la fonction rappelle 

        items = [{ #Ca c'est pour Ouverture ou fermerture ou DD
            "text":"O",
            "on_release":lambda x = "O" : self.Clic(x)
        },
        {
            "text":"F",
            "on_release":lambda x = "F" : self.Clic(x)
        },
        {
            "text":"DD",
            "on_release":lambda x = "DD" : self.Clic(x)
        }
        ]
        self.Operation = MDDropdownMenu(
            caller = Pge.Page3_4,
            items = items,
            width_mult = 3,
        )

        Pge.Page3_4.bind(on_touch_down = self.Open_Menu)
        
       
    def Open_Menu(self, instance, touch):
        if instance.collide_point(*touch.pos):
            self.Operation.open()
            return True
        return False
    
    def Clic(self,x):
        Pge = self.cr.current_screen.ids
        self.Operation.dismiss()
        Pge.Page3_4.text = x
        
    #Fonction valider pour la Page3
    def Valider_3(self,instance):
        Pge = self.cr.current_screen.ids
        Liste = [Pge.Page3_2,Pge.Page3_3,Pge.Page3_4,Pge.Page3_5]
        Error = False
        for elmt in Liste:
            if elmt.text =="":
                elmt.error = True
                Error = True
        
        if not Error:
            try:
                Pge = self.cr.current_screen.ids
                Liste2 = [Pge.Page3_2,Pge.Page3_3,Pge.Page3_4,Pge.Page3_5,Pge.Page3_6]
                cur = self.con.cursor()
                cur.execute("Insert into BCC (Date,Operator,O_F_DD,Operation,Mension) values (?,?,?,?,?)",tuple([elmt.text for elmt in Liste2]))
                self.con.commit()

                toast("Ajout effectué avec succes!")
            except:
                toast("Error !")

    def Recharge_date(self,instance):
        cur = self.con.cursor()
        Tous = cur.execute("SELECT * FROM  BCC")

        Date = set()
        for elmt in Tous:
            Date.add(elmt[1])
        
        items = []
        for elmt in Date:
            dic = {
                "text":elmt,
                "on_release": lambda btn = instance,x = elmt : self.Select2(btn,x)
            }
            items.append(dic)

        self.Operation2 = MDDropdownMenu(
            caller = instance,
            items = items,
            width_mult = 5,
        )

        self.Operation2.open()

    def Select2(self,instance,x):
        instance.text = f"[b]{x}[/b]"
        self.DATE = x
        self.page4()
        self.Operation2.dismiss()

    def page4(self):
        cur = self.con.cursor()
        Tous = cur.execute("SELECT * FROM BCC")
        
        Pge = self.cr.current_screen.ids
        Liste1 = [Pge.Page2_7,Pge.Page2_9,Pge.Page2_8,Pge.Page2_10,Pge.Page2_11]
        for elmt in Liste1:
            elmt.theme_icon_color = "Custom"
            if Liste1.index(elmt) == 3:
                elmt.icon_color = [1,1,1,1]
            else:
                elmt.icon_color = [0,0,0,1]

        Pge.Page4_But.text = f"[b]{self.DATE}[/b]"
        Veux = []
        for elmt in Tous:
            if elmt[1] == self.DATE:
                Veux.append(list(elmt))
        
        #try:
        Ici = self.cr.current_screen.ids.Page4_2
        if Veux:  # Si on a des données
            if self.PAGE4_Liste == [] or self.PAGE4_Liste != Veux:
                self.PAGE4_Liste = Veux
                Ici.clear_widgets()
                Ici.add_widget(self.create_data_table(Veux))
                
                
        else:  # Si pas de données
            Ici.clear_widgets()
            Ici.add_widget(self.create_empty_message())
        #except:
            #pass
     
    def create_data_table(self, data):
        # Définir les noms des colonnes (correspondant à la table BCC)
        column_data = [
            ("ID", dp(20)),
            ("Date", dp(30)),
            ("Opérateur", dp(30)),
            ("O/F/DD", dp(20)),
            ("Opération", dp(50)),
            ("Mention", dp(30))
        ]
        # Convertir les données en tuples pour MDDataTable
        row_data = [tuple(row) for row in data]
        # Créer le MDDataTable
        data_table = MDDataTable(
            size_hint=(1, 1),
            column_data=column_data,
            row_data=row_data,
            elevation=2,
            use_pagination=True,  # Activer la pagination si beaucoup de données
            rows_num=10,  # Nombre de lignes par page
            on_row_press=lambda *args: None,
            check=False  # Désactiver les cases à cocher (optionnel)
            
        )
        
        return data_table

    def Appui_Icon_page2(self, instance):
        Pge = self.cr.current_screen.ids
        Liste = [Pge.Page2_4, Pge.Page2_5, Pge.Page2_6, Pge.Page2_11]
        Liste = [elmt.text for elmt in Liste]
        self.Liste = Liste
        print(Liste)
        Icons = ["web", 'information', "brightness-6", "palette"]
        
        Items = []
        for elmt1, elmt2 in zip(Liste, Icons):
            Add = {
                "text": elmt1,
                "icon": elmt2,
                # CORRECTION: Utiliser une lambda pour passer les bons arguments
                "on_release": lambda btn = instance , text=elmt1: self.Faire_Icon(btn, text)
            }
            Items.append(Add)

        self.INSTANCE = instance
        
        self.Operation3 = MDDropdownMenu(
            caller=instance,
            items=Items,
            width_mult=3,
        )
        
        instance.icon = "close"
        self.Operation3.open()
    
    def create_empty_message(self):
        """Créer un message quand il n'y a pas de données"""
        
        layout = MDBoxLayout(
            orientation="vertical",
            spacing="20dp",
            adaptive_height=True,
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        
        # Message principal
        message = MDLabel(
            text=f"Aucune donnée pour le {self.DATE}",
            halign="center",
            theme_text_color="Primary",
            font_style="H6"
        )
        
        # Message secondaire
        submessage = MDLabel(
            text="Ajoutez des opérations pour voir les données ici",
            halign="center",
            theme_text_color="Secondary",
            font_style="Caption"
        )
        
        # Bouton pour ajouter des données (optionnel)
        add_button = MDRaisedButton(
            text="[b]Ajouter une opération[/b]",
            pos_hint={"center_x": 0.5},
            on_release=lambda x: self.Next_But(None, 3)  # Aller à la page de saisie
        )
        
        layout.add_widget(message)
        layout.add_widget(submessage)
        layout.add_widget(add_button)
        
        return layout

    # Fonction corrigée pour accepter les bons paramètres
    def Faire_Icon(self, instance,x):
        """
        calling_button: Le bouton qui a ouvert le menu
        menu_item: L'item du menu qui a été cliqué
        selected_text: Le texte de l'item sélectionné
        """
        #x = selected_text  # ou menu_item.text si vous préférez
        
        dic = {
            self.Liste[0]: self.Changer_language,
            self.Liste[1]: None,
            self.Liste[2]: self.Changer_font1,
            self.Liste[-1]: self.Changer_font2
        }
        
        func = dic.get(x)
        if func is not None:
            func(instance)  # Passer le bouton original
    
        # Fermer le menu et remettre l'icône
        self.Operation3.dismiss()
        self.INSTANCE.icon = "plus"

    def page2(self):
        Element = self.Langue.get(self.Current_lang).get("Page2")
        Pge = self.cr.current_screen.ids

        Liste1 = [Pge.Page2_7,Pge.Page2_9,Pge.Page2_8,Pge.Page2_10]
        for elmt in Liste1:
            elmt.theme_text_color = "Custom"
            if Liste1.index(elmt) == 1:
                elmt.icon_color = [1,1,1,1]
            else:
                elmt.icon_color = [0,0,0,1]

        Liste = [Pge.Page2_1,Pge.Page2_2,Pge.Page2_3,Pge.Page2_5,Pge.Page2_6,Pge.Page2_7,Pge.Page2_8,Pge.Page2_9,Pge.Page2_10]

        Pge.Page2_4.text = self.Current_lang

        for elmt,elmt2 in zip(Liste,Element.keys()):
            elmt.text = Element.get(elmt2)
    
    def Add(self,instance):
        self.Next(3)
    
    def history(self,instance):
        self.Next(4)
        
    def Changer_language(self, instance):
        self.langues_disponibles = [
            {"text": "Français", "code": "fr"},
            {"text": "English", "code": "en"},
            {"text": "Español", "code": "es"},
            {"text": "Deutsch", "code": "de"},
            {"text": "中文 (简体)", "code": "zh"},
            {"text": "中文 (繁體)", "code": "zh-tw"},
            {"text": "日本語", "code": "ja"},
            {"text": "한국어", "code": "ko"},
            {"text": "العربية", "code": "ar"},
            {"text": "Русский", "code": "ru"},
            {"text": "Português", "code": "pt"},
            {"text": "Italiano", "code": "it"},
        ]
        
        menu = []
        for elmt in self.langues_disponibles:
            menu.append(
                {
                    "text":elmt["text"],
                    "on_release":lambda x = elmt["code"],btn = instance : self.selecter_Lang(btn,x)
                }
            )
        
        self.Menu = MDDropdownMenu(
            caller=instance,
            items=menu,
            width_mult=4,  # ← Correction 6: width_mult, pas width_milt
            max_height=dp(200),
            border_margin=dp(8),
        )
        
        self.Menu.open()
    
    def selecter_Lang(self,instance,code):
        #dic = {"[b]fr[/b]":"en" , "[b]en[/b]":"fr"}
        self.Current_lang = code#dic.get(instance.text)
        instance.text = f"[b]{self.Current_lang}[/b]"
        self.Menu.dismiss()
    
    def Go(self,intance):
        self.Next()
    
    def Next(self,val = None):
        Pge = self.cr.current
        self.cr.current = f"Page{int(Pge.split('e')[-1])+1 if val == None else val}"
    
    def Next_But(self,intance,val = None):
        self.Next(val)
        

BCC().run()
