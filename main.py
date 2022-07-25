from tkinter import *
import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\burgercafe-app\\')


class App():
    def __init__(self): 
        self.root = Tk()
        self.x = int(self.root.winfo_screenwidth() // 2.3)
        self.y = int(self.root.winfo_screenheight() * 0.2)
        self.x, self.y = str(self.x), str(self.y)
        self.root.geometry(f'350x500+{self.x}+{self.y}')
        self.root.title('Burger Cafe')
        self.root.resizable(0, 0)
        # self.root.attributes('-alpha', 0.8)
        self.root.iconbitmap('assets\\logo.ico')
        
        self.font = ('TkMenuFont',10)
        self.header_font = ('TkMenuFont',10, 'bold')
        self.price_font = ('TkMenuFont',12, 'bold')
        self.bgcolor = '#fede00'
        self.fgcolor = '#000000'
        self.menu_fgcolor = '#b29b00'
        self.button_hovercolor = '#edd002'
        self.order_dict = {}
        self.showHome()
        self.root.mainloop()
        
        
    def showBackground(self):
        self.bg = Label(self.root, background = self.bgcolor)
        self.bg.place(width = 350, height = 500)
    
    
    def hover(self, btn, colorOnHover, colorOnLeave, colorfgOnHover, colorfgOnLeave):
        btn.bind("<Enter>", func = lambda i: btn.config(background = colorOnHover, foreground = colorfgOnHover))
        btn.bind("<Leave>", func = lambda i: btn.config(background = colorOnLeave, foreground = colorfgOnLeave))
        
        
    def showHome(self):
        self.showBackground()
        self.logo = PhotoImage(file = 'assets\\logo.png')
        self.logowidget = Label(self.root, image = self.logo, background = self.bgcolor)
        self.logowidget.place(x = 80, y = 5)
        self.decor = PhotoImage(file = 'assets\\decor.png')
        self.decorwidget = Label(self.root, image = self.decor, background = self.bgcolor)
        self.decorwidget.place(x = 60, y = 250)
        self.showMenu()
        self.showUser()
        self.showWeb()
    
    
    def showMenu(self):
        self.button_aboutus = Button(self.root, text = 'ABOUT US', command = self.showAboutUs)
        self.button_aboutus.place(x = 20, y = 200, width = 80, height = 25)
        self.button_menu = Button(self.root, text = 'MENU', command = self.showPage1)
        self.button_menu.place(x = 20, y = 225, width = 80, height = 25)
        self.button_recipes = Button(self.root, text = 'RECIPES', command = self.showRecipes)
        self.button_recipes.place(x = 20, y = 250, width = 80, height = 25)
        self.button_contacts = Button(self.root, text = 'CONTACTS', command = self.showContacts)
        self.button_contacts.place(x = 20, y = 275, width = 80, height = 25)
        self.basketButton = Button(self.root, text = '🛒', command = self.bill)
        self.basketButton.place(x = 45, y = 20, width = 25, height = 25)
        
        for i in (self.button_aboutus, self.button_menu, self.button_recipes, self.button_contacts, self.basketButton):
            i.configure(
            background = self.bgcolor,
            foreground = self.fgcolor,
            font = self.font,
            anchor = "w",
            relief = 'flat',
            cursor = 'hand2',
            activebackground = self.bgcolor,
            activeforeground = self.menu_fgcolor
            )
            self.hover(i, self.button_hovercolor, self.bgcolor, self.menu_fgcolor, self.fgcolor)
    
    
    def showUser(self):
        self.button = Button(self.root, text = '👤', command = self.close)
        self.button.configure(
            background = self.bgcolor,
            foreground = self.fgcolor,
            font = self.font,
            relief = 'flat',
            cursor = 'hand2',
            activebackground = self.bgcolor,
            activeforeground = self.menu_fgcolor
            )
        self.hover(self.button, self.button_hovercolor, self.bgcolor, self.menu_fgcolor, self.fgcolor)
        self.button.place(x = 305, y = 20, width = 25, height = 25)
    
    
    def showWeb(self):
        self.button = Button(self.root, text = '🌐', command = self.close)
        self.button.configure(
            background = self.bgcolor,
            foreground = self.fgcolor,
            font = self.font,
            relief = 'flat',
            cursor = 'hand2',
            activebackground = self.bgcolor,
            activeforeground = self.menu_fgcolor
            )
        self.hover(self.button, self.button_hovercolor, self.bgcolor, self.menu_fgcolor, self.fgcolor)
        self.button.place(x = 20, y = 20, width = 25, height = 25)
    
    
    def showPage1(self):
        try:
            self.values2 = (self.output_applepie, self.output_browniecake, self.output_cola)
            self.names_page2 = ('Apple Pie','Brownie','Cola')
            for i in range(0, len(self.values2)):
                self.order_dict[self.names_page2[i]] = self.values2[i]['text']
        except AttributeError:
            pass
        
        self.page = 1
        self.showBackground()
        self.showClose()
        self.burger = PhotoImage(file = 'assets\\burger.png')
        self.cupcake = PhotoImage(file = 'assets\\cupcake.png')
        self.pancake = PhotoImage(file = 'assets\\pancake.png')
        self.burgerwidget = Label(self.root, image = self.burger, background = self.bgcolor)
        self.burgerwidget.place(x = 150, y = -30)
        self.pancakewidget = Label(self.root, image = self.pancake, background = self.bgcolor)
        self.pancakewidget.place(x = -130, y = 160)
        self.cupcakewidget = Label(self.root, image = self.cupcake, background = self.bgcolor)
        self.cupcakewidget.place(x = 200, y = 300)
        self.header_burgerwidget = Label(self.burgerwidget, text = '', background = self.bgcolor, font = self.header_font, justify = LEFT, wraplength = 150)
        self.header_burgerwidget['text'] = 'Burger with Vegetables'
        self.text_burgerwidget = Label(self.root, text = '', background = self.bgcolor, font = self.font, justify = LEFT, wraplength = 140)
        self.text_burgerwidget['text'] = 'Enjoy deliciously simple craft Classic Burger with a juicy beef patty, lettuce, tomato, onions and pickles on a bun.'
        self.header_burgerwidget.place(x = 0, y = 50, width = 160)
        self.text_burgerwidget.place(x = 25, y = 50, width = 140)
        
        self.header_pancakewidget = Label(self.pancakewidget, text = '', background = self.bgcolor, font = self.header_font, justify = LEFT, wraplength = 170)
        self.header_pancakewidget['text'] = 'Pancakes with Blueberries'
        self.text_pancakewidget = Label(self.root, text = '', background = self.bgcolor, font = self.font, justify = LEFT, wraplength = 110)
        self.text_pancakewidget['text'] = 'Thick and fluffy pancakes! Melt in your mouth, golden brown, and bursting with blueberries.'
        self.header_pancakewidget.place(x = 150, y = 20, width = 180)
        self.text_pancakewidget.place(x = 200, y = 203, width = 110)
        
        self.header_cupcakewidget = Label(self.cupcakewidget, text = '', background = self.bgcolor, font = self.header_font, justify = LEFT, wraplength = 130)
        self.header_cupcakewidget['text'] = 'Chocolate Cupcake'
        self.text_cupcakewidget = Label(self.root, text = '', background = self.bgcolor, font = self.font, justify = LEFT, wraplength = 160)
        self.text_cupcakewidget['text'] = 'These delicious cupcake has a chocolate centre once you get past the cream topping.'
        self.header_cupcakewidget.place(x = 0, y = 80, width = 130)
        self.text_cupcakewidget.place(x = 25, y = 405, width = 150)
        
        self.output_burgerwidget = Message(self.root, text = '0', background = self.bgcolor, width = 5)
        self.output_burgerwidget.place(x = 174, y = 150)
        self.output_pancakewidget = Message(self.root, text = '0', background = self.bgcolor, width = 5)
        self.output_pancakewidget.place(x = 150, y = 345)
        self.output_cupcakewidget = Message(self.root, text = '0', background = self.bgcolor, width = 5)
        self.output_cupcakewidget.place(x = 208, y = 470)
        
        self.next_button = Button(self.root, text = '>', command = self.showPage2)
        self.next_button.configure(
            background = self.bgcolor,
            foreground = self.fgcolor,
            font = self.font,
            relief = 'flat',
            cursor = 'hand2',
            activebackground = self.bgcolor,
            activeforeground = self.menu_fgcolor
            )
        self.hover(self.next_button, self.button_hovercolor, self.bgcolor, self.menu_fgcolor, self.fgcolor)
        self.next_button.place(x = 305, y = 225, width = 25, height = 25)
        
        self.showPrice()
        self.showIncrease()
        self.showDecrease()
    
    
    def showPage2(self):
        self.page = 2
        
        self.values1 = (self.output_burgerwidget, self.output_pancakewidget, self.output_cupcakewidget)
        self.names_page1 = ('Burger','Pancake','Cupcake')
        for i in range(0, len(self.values1)):
            self.order_dict[self.names_page1[i]] = self.values1[i]['text']    
        
        self.showBackground()
        self.showClose()
        self.applepie = PhotoImage(file = 'assets\\applepie.png')
        self.browniecake = PhotoImage(file = 'assets\\browniecake.png')
        self.cola = PhotoImage(file = 'assets\\cola.png')
        self.applepiewidget = Label(self.root, image = self.applepie, background = self.bgcolor)
        self.applepiewidget.place(x = 130, y = -60)
        self.browniecakewidget = Label(self.root, image = self.browniecake, background = self.bgcolor)
        self.browniecakewidget.place(x = -60, y = 160)
        self.colawidget = Label(self.root, image = self.cola, background = self.bgcolor)
        self.colawidget.place(x = 180, y = 300)
        
        self.header_applepie = Label(self.applepiewidget, text = '', background = self.bgcolor, font = self.header_font, justify = LEFT, wraplength = 100)
        self.header_applepie['text'] = 'Apple Pie'
        self.text_applepie = Label(self.root, text = '', background = self.bgcolor, font = self.font, justify = LEFT, wraplength = 100)
        self.text_applepie['text'] = "This is absolutely the best homemade apple pie you'll ever taste!"
        self.header_applepie.place(x = 30, y = 80, width = 100)
        self.text_applepie.place(x = 25, y = 50, width = 110)
        
        self.header_browniecake = Label(self.browniecakewidget, text = '', background = self.bgcolor, font = self.header_font, justify = LEFT, wraplength = 100)
        self.header_browniecake['text'] = 'Brownie Cake'
        self.text_browniecake = Label(self.root, text = '', background = self.bgcolor, font = self.font, justify = LEFT, wraplength = 110)
        self.text_browniecake['text'] = 'These delightful individual Chocolate Brownie cakes are the perfect mini treat.'
        self.header_browniecake.place(x = 130, y = 20, width = 100)
        self.text_browniecake.place(x = 200, y = 203, width = 110)
        
        self.header_cola = Label(self.colawidget, text = '', background = self.bgcolor, font = self.header_font, justify = LEFT, wraplength = 130)
        self.header_cola['text'] = 'Refreshing Cola'
        self.text_cola = Label(self.root, text = '', background = self.bgcolor, font = self.font, justify = LEFT, wraplength = 160)
        self.text_cola['text'] = 'Refreshing a sugar-free drink that looks and tastes like the classic Cola.'
        self.header_cola.place(x = 0, y = 80, width = 130)
        self.text_cola.place(x = 25, y = 405, width = 160)
        
        self.output_applepie = Message(self.root, text = '0', background = self.bgcolor, width = 5)
        self.output_applepie.place(x = 174, y = 150)
        self.output_browniecake = Message(self.root, text = '0', background = self.bgcolor, width = 5)
        self.output_browniecake.place(x = 150, y = 345)
        self.output_cola = Message(self.root, text = '0', background = self.bgcolor, width = 5)
        self.output_cola.place(x = 208, y = 470)
        
        self.previous_button = Button(self.root, text = '<', command = self.showPage1)
        self.previous_button.configure(
            background = self.bgcolor,
            foreground = self.fgcolor,
            font = self.font,
            relief = 'flat',
            cursor = 'hand2',
            activebackground = self.bgcolor,
            activeforeground = self.menu_fgcolor
            )
        self.hover(self.previous_button, self.button_hovercolor, self.bgcolor, self.menu_fgcolor, self.fgcolor)
        self.previous_button.place(x = 20, y = 225, width = 25, height = 25)
        
        self.pricewidget1 = Label(self.applepiewidget, text = '$1.65', background = self.bgcolor, font = self.price_font, justify = LEFT, wraplength = 45)
        self.pricewidget2 = Label(self.browniecakewidget, text = '$1.99', background = self.bgcolor, font = self.price_font, justify = LEFT, wraplength = 45)
        self.pricewidget3 = Label(self.colawidget, text = '$0.99', background = self.bgcolor, font = self.price_font, justify = LEFT, wraplength = 45)
        self.pricewidget1.place(x = 45, y = 100, width = 50, height = 25)
        self.pricewidget2.place(x = 180, y = 42, width = 50, height = 25)
        self.pricewidget3.place(x = 0, y = 102, width = 50, height = 25)
        self.showIncrease()
        self.showDecrease()
    
    
    def showClose(self):
        self.button = Button(self.root, text = 'x', command = self.close)
        self.button.configure(
            background = self.bgcolor,
            foreground = self.fgcolor,
            font = self.font,
            relief = 'flat',
            cursor = 'hand2',
            activebackground = self.bgcolor,
            activeforeground = self.menu_fgcolor
            )
        self.hover(self.button, self.button_hovercolor, self.bgcolor, self.menu_fgcolor, self.fgcolor)
        self.button.place(x = 20, y = 20, width = 25, height = 25)

    
    def showNext(self, i):
        if i == 'burger':
            self.button = Button(self.root, text = '>', command = lambda:self.showRecipe('pancake'))
        elif i == "pancake":
            self.button = Button(self.root, text = '>', command = lambda:self.showRecipe('cupcake'))
        else:
            self.button = Button(self.root, text = '>', command = lambda:self.showRecipe('burger'))
        self.button.configure(
            background = self.bgcolor,
            foreground = self.fgcolor,
            font = self.font,
            relief = 'flat',
            cursor = 'hand2',
            activebackground = self.bgcolor,
            activeforeground = self.menu_fgcolor
            )
        self.hover(self.button, self.button_hovercolor, self.bgcolor, self.menu_fgcolor, self.fgcolor)
        self.button.place(x = 305, y = 225, width = 25, height = 25)
        
    
    def showPrevious(self, i):
        if i == 'burger':
            self.button = Button(self.root, text = '<', command = lambda:self.showRecipe('cupcake'))
        elif i == "cupcake":
            self.button = Button(self.root, text = '<', command = lambda:self.showRecipe('pancake'))
        else:
            self.button = Button(self.root, text = '<', command = lambda:self.showRecipe('burger'))
        self.button.configure(
            background = self.bgcolor,
            foreground = self.fgcolor,
            font = self.font,
            relief = 'flat',
            cursor = 'hand2',
            activebackground = self.bgcolor,
            activeforeground = self.menu_fgcolor
            )
        self.hover(self.button, self.button_hovercolor, self.bgcolor, self.menu_fgcolor, self.fgcolor)
        self.button.place(x = 20, y = 225, width = 25, height = 25)
        
    
    def showBack(self):
        self.button = Button(self.root, text = '<', command = self.showRecipes)
        self.button.configure(
            background = self.bgcolor,
            foreground = self.fgcolor,
            font = self.font,
            relief = 'flat',
            cursor = 'hand2',
            activebackground = self.bgcolor,
            activeforeground = self.menu_fgcolor
            )
        self.hover(self.button, self.button_hovercolor, self.bgcolor, self.menu_fgcolor, self.fgcolor)
        self.button.place(x = 45, y = 20, width = 25, height = 25)
    
    
    def showPrice(self):
        self.pricewidget1 = Label(self.burgerwidget, text = '$2.50', background = self.bgcolor, font = self.price_font, justify = LEFT, wraplength = 45)
        self.pricewidget2 = Label(self.pancakewidget, text = '$6.75', background = self.bgcolor, font = self.price_font, justify = LEFT, wraplength = 45)
        self.pricewidget3 = Label(self.cupcakewidget, text = '$2.15', background = self.bgcolor, font = self.price_font, justify = LEFT, wraplength = 45)
        self.pricewidget1.place(x = 10, y = 72, width = 50, height = 25)
        self.pricewidget2.place(x = 275, y = 42, width = 50, height = 25)
        self.pricewidget3.place(x = 0, y = 102, width = 50, height = 25)
    
    
    def showBasket(self):
        if self.page == 1:
            for i in (self.output_burgerwidget, self.output_pancakewidget, self.output_cupcakewidget):
                if int(i['text']) > 0:
                    self.basketButton = Button(self.root, text = '🛒', command = self.count)
        else:
             for i in (self.output_applepie, self.output_browniecake, self.output_cola):
                if int(i['text']) > 0:
                    self.basketButton = Button(self.root, text = '🛒', command = self.count)
        self.basketButton.configure(
                        background = self.bgcolor,
                        foreground = self.fgcolor,
                        font = self.font,
                        relief = 'flat',
                        cursor = 'hand2',
                        activebackground = self.bgcolor,
                        activeforeground = self.menu_fgcolor
                        )
        self.hover(self.basketButton, self.button_hovercolor, self.bgcolor, self.menu_fgcolor, self.fgcolor)
        self.basketButton.place(x = 45, y = 20, width = 25, height = 25)
        
        
    def showIncrease(self):
        self.increaseButton1 = Button(self.root, text = '+', command = lambda:self.increase(1, 'increaseButton1'))
        self.increaseButton2 = Button(self.root, text = '+', command = lambda:self.increase(1, 'increaseButton2'))
        self.increaseButton3 = Button(self.root, text = '+', command = lambda:self.increase(1, 'increaseButton3'))
        for i in (self.increaseButton1, self.increaseButton2, self.increaseButton3):
            i.configure(
            background = self.bgcolor,
            foreground = self.fgcolor,
            font = self.font,
            relief = 'flat',
            cursor = 'hand2',
            activebackground = self.bgcolor,
            activeforeground = self.menu_fgcolor
            )
            self.hover(i, self.button_hovercolor, self.bgcolor, self.menu_fgcolor, self.fgcolor)
        self.increaseButton1.place(x = 197, y = 149, width = 25, height = 25)
        self.increaseButton2.place(x = 173, y = 344, width = 25, height = 25)
        self.increaseButton3.place(x = 231, y = 469, width = 25, height = 25)
    
    
    def showDecrease(self):
        self.decreaseButton1 = Button(self.root, text = '-', command = lambda:self.decrease(1, 'decreaseButton1'))
        self.decreaseButton2 = Button(self.root, text = '-', command = lambda:self.decrease(1, 'decreaseButton2'))
        self.decreaseButton3 = Button(self.root, text = '-', command = lambda:self.decrease(1, 'decreaseButton3'))
        for i in (self.decreaseButton1, self.decreaseButton2, self.decreaseButton3):
            i.configure(
            background = self.bgcolor,
            foreground = self.fgcolor,
            font = self.font,
            relief = 'flat',
            cursor = 'hand2',
            activebackground = self.bgcolor,
            activeforeground = self.menu_fgcolor
            )
            self.hover(i, self.button_hovercolor, self.bgcolor, self.menu_fgcolor, self.fgcolor)
        self.decreaseButton1.place(x = 146, y = 149, width = 25, height = 25)
        self.decreaseButton2.place(x = 122, y = 344, width = 25, height = 25)
        self.decreaseButton3.place(x = 180, y = 469, width = 25, height = 25)

            
    def increase(self, i, y):
        self.val = int(i)
        if self.page == 1:
            if y == 'increaseButton1' and int(self.output_burgerwidget['text']) < 9:
                self.val += int(self.output_burgerwidget['text'])
                self.output_burgerwidget['text'] = str(self.val)
                self.showBasket()
            elif y == 'increaseButton2' and int(self.output_pancakewidget['text']) < 9:
                self.val += int(self.output_pancakewidget['text'])
                self.output_pancakewidget['text'] = str(self.val)
                self.showBasket()
            elif y == 'increaseButton3' and int(self.output_cupcakewidget['text']) < 9:
                self.val += int(self.output_cupcakewidget['text'])
                self.output_cupcakewidget['text'] = str(self.val)
                self.showBasket()
        else:
            if y == 'increaseButton1' and int(self.output_applepie['text']) < 9:
                self.val += int(self.output_applepie['text'])
                self.output_applepie['text'] = str(self.val)
                self.showBasket()
            elif y == 'increaseButton2' and int(self.output_browniecake['text']) < 9:
                self.val += int(self.output_browniecake['text'])
                self.output_browniecake['text'] = str(self.val)
                self.showBasket()
            elif y == 'increaseButton3' and int(self.output_cola['text']) < 9:
                self.val += int(self.output_cola['text'])
                self.output_cola['text'] = str(self.val)
                self.showBasket()
    
            
    def decrease(self, i, y):
        self.val = int(i)
        if self.page == 1:
            if y == 'decreaseButton1' and int(self.output_burgerwidget['text']) != 0:
                x = int(self.output_burgerwidget['text'])
                x -= self.val
                self.output_burgerwidget['text'] = str(x)
            elif y == 'decreaseButton2' and int(self.output_pancakewidget['text']) != 0:
                x = int(self.output_pancakewidget['text'])
                x -= self.val
                self.output_pancakewidget['text'] = str(x)
            elif y == 'decreaseButton3' and int(self.output_cupcakewidget['text']) != 0:
                x = int(self.output_cupcakewidget['text'])
                x -= self.val
                self.output_cupcakewidget['text'] = str(x)
        else:
            if y == 'decreaseButton1' and int(self.output_applepie['text']) != 0:
                x = int(self.output_applepie['text'])
                x -= self.val
                self.output_applepie['text'] = str(x)
            elif y == 'decreaseButton2' and int(self.output_browniecake['text']) != 0:
                x = int(self.output_browniecake['text'])
                x -= self.val
                self.output_browniecake['text'] = str(x)
            elif y == 'decreaseButton3' and int(self.output_cola['text']) != 0:
                x = int(self.output_cola['text'])
                x -= self.val
                self.output_cola['text'] = str(x)
        
    
    def showAboutUs(self):
        self.showBackground()
        self.showClose()
        self.decor = PhotoImage(file = 'assets\\decor_about_us.png')
        self.decorwidget = Label(self.root, image = self.decor, background = self.bgcolor)
        self.decorwidget.place(x = 60, y = 250)
        self.text_widget = Label(self.root, text = '', background = self.bgcolor, font = self.font, justify = LEFT, wraplength = 260)
        self.text_widget['text'] = 'Welcome to Burger Cafe!\n\nHome of the best burgers. Located in the beautiful city, Burger Cafe is a family-friendly cafe that serves the best burgers with refreshing cola. You will be delighted with our apple pie, brownie, pancakes and cupcakes.\n\nAll of our products are prepared with the finest and freshest ingredients!'
        self.text_widget.place(x = 45, y = 50, width = 260)
        
    
    def showRecipes(self):
        self.showBackground()
        self.showClose()
        self.decor = PhotoImage(file = 'assets\\decor_recipes.png')
        self.decorwidget = Label(self.root, image = self.decor, background = self.bgcolor)
        self.decorwidget.place(x = 60, y = 250)
        self.recipe1 = Button(self.root, text = 'BURGERS WITH VEGETABLES', command = lambda:self.showRecipe('burger'))
        self.recipe2 = Button(self.root, text = 'PANCAKE WIHT BLUEBERRIES', command = lambda:self.showRecipe('pancake'))
        self.recipe3 = Button(self.root, text = 'CHOCOLATE CUPCAKES', command = lambda:self.showRecipe('cupcake'))
        
        for i in (self.recipe1, self.recipe2, self.recipe3):
            i.configure(
            background = self.bgcolor,
            foreground = self.fgcolor,
            font = self.font,
            anchor = "w",
            relief = 'flat',
            cursor = 'hand2',
            activebackground = self.bgcolor,
            activeforeground = self.menu_fgcolor
            )
            self.hover(i, self.button_hovercolor, self.bgcolor, self.menu_fgcolor, self.fgcolor)
        self.recipe1.place(x = 70, y = 50, width = 205, height = 25)
        self.recipe2.place(x = 70, y = 75, width = 205, height = 25)
        self.recipe3.place(x = 70, y = 100, width = 205, height = 25)
        
    
    def showRecipe(self, i):
        self.showBackground()
        self.showClose()
        self.showNext(i)
        self.showPrevious(i)
        self.text_widget = Label(self.root, text = '', background = self.bgcolor, font = self.font, justify = LEFT, wraplength = 260)
        self.header_widget = Label(self.root, text = '', background = self.bgcolor, font = self.header_font, justify = LEFT, wraplength = 260)
        if i == 'burger':
            self.header_widget['text'] = 'Burger with Vegetables'
            self.text_widget['text'] = 'Ingredients:\n* 1 small onion, diced,* 500g good-quality beef mince,* 1 egg,* 1 tbsp vegetable oil,* 4 burger buns,* all or any of the following to serve: sliced tomato, beetroot, horseradish sauce, mayonnaise, ketchup, handful iceberg lettuce, rocket, watercress\n\nMethod:\nTip 500g beef mince into a bowl with 1 small diced onion and 1 egg, then mix. Divide the mixture into four. Roll the mixture into balls and squeeze down to flatten into patties. Put on a plate, cover with cling film and leave in the fridge to firm up for at least 30 mins. Heat the barbecue to medium hot. Lightly brush one side of each burger with vegetable oil. Place the burgers, oil-side down, on the barbecue. Cook for 5 mins until the meat is lightly charred. Oil the other side, then turn over using tongs. Slice four burger buns in half. Place, cut-side down, on the barbecue rack and toast for 1 min until they are lightly charred. Place a burger inside each bun.'
        elif i == 'pancake':
            self.header_widget['text'] = 'Pancakes with Blueberries'
            self.text_widget['text'] = 'Ingredients:\n* 200g self-raising flour,* 1 tsp baking powder,* 1 egg,* 300ml milk,* knob butter,* 150g pack blueberry,* sunflower oil or a little butter for cooking,* golden or maple syrup\n\nMethod:\nMix together 200g self-raising flour, 1 tsp baking powder and a pinch of salt in a large bowl. Beat 1 egg with 300ml milk, make a well in the centre of the dry ingredients and whisk in the milk to make a thick smooth batter. Beat in a knob of melted butter, and stir in half of the 150g pack of blueberries. Heat a teaspoon of sunflower oil or small knob of butter in a frying pan. Drop a large tablespoonful of the batter per pancake into the pan to make pancakes about 7.5cm across. Cook for about 3 minutes over a medium heat, then turn and cook another 2-3 minutes until golden. Cover with kitchen paper to keep warm while you use up the rest of the batter. Serve with golden or maple syrup and the rest of the blueberries.'
        else:
            self.header_widget['text'] = 'Chocolate Cupcakes'
            self.text_widget['text'] = 'Ingredients:\n* 110g softened butter,* 110g golden caster sugar,* 2 large eggs,* ½ tsp vanilla extract,* 110g self-raising flour,* 150g softened butter,* 300g icing sugar,* 1 tsp vanilla extract,* 3 tbsp milk\n\nMethod:\nHeat oven to 180C/160C fan/gas and fill a 12 cupcake tray with cases. Using a whisk beat 110g softened butter and 110g golden caster sugar together until pale and fluffy then whisk in 2 large eggs, one at a time, scraping down the sides of the bowl after each addition. Add ½ tsp vanilla extract, 110g self-raising flour and a pinch of salt, whisk until just combined then spoon the mixture into the cupcake cases. Bake for 15 mins until golden brown and a skewer inserted into the middle of each cake comes out clean. To make the buttercream, whisk 150g softened butter until super soft then add 300g icing sugar, 1 tsp vanilla extract and a pinch of salt. Whisk together until smooth then beat in 3 tbsp milk.'
        self.header_widget.place(x = 45, y = 35, width = 260)
        self.text_widget.place(x = 45, y = 65, width = 260)
        self.showBack()
        
    
    def showContacts(self):
        self.showBackground()
        self.showClose()
        self.decor = PhotoImage(file = 'assets\\decor_contacts.png')
        self.decorwidget = Label(self.root, image = self.decor, background = self.bgcolor)
        self.decorwidget.place(x = 60, y = 250)
        self.text_widget = Label(self.root, text = '', background = self.bgcolor, font = self.font, justify = LEFT, wraplength = 260)
        self.text_widget['text'] = 'Schedule & Contacts.\n\nBurger Cafe is open 7 days a week & offers delivery.'
        self.text_widget.place(x = 45, y = 50, width = 260)
        
    
    def count(self):
        if self.page == 1:
            self.values1 = (self.output_burgerwidget, self.output_pancakewidget, self.output_cupcakewidget)
            self.names_page1 = ('Burger','Pancake','Cupcake')
            for i in range(0, len(self.values1)):
                self.order_dict[self.names_page1[i]] = self.values1[i]['text']
        else:
            self.values2 = (self.output_applepie, self.output_browniecake, self.output_cola)
            self.names_page2 = ('Apple Pie','Brownie','Cola')
            for i in range(0, len(self.values2)):
                self.order_dict[self.names_page2[i]] = self.values2[i]['text']
        self.bill()
        
        
    def bill(self):
        self.showBackground()
        self.showClose()
        print(self.order_dict)
        
        
    def close(self):
        try:
            for i in (self.decorwidget,self.text_widget,self.burgerwidget,self.pancakewidget,self.recipe1,self.recipe2,self.recipe3,self.button):
                i.destroy()
        except AttributeError:
            pass
        self.order_dict = {}
        self.showHome()

if __name__ == '__main__':
    App()