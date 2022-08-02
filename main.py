from tkinter import *
import pyglet
import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\burgercafe-app\\')
pyglet.font.add_file('C:\\Users\\baben\\Documents\\GitHub\\burgercafe-app\\fonts\\Pacifico.ttf')

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
        
        self.accent_font_1 = ('TkMenuFont',10)
        self.accent_font_2 = ('TkMenuFont',12, 'bold')
        self.accent_font_3 = ('Pacifico', 14)
        self.accent_color_1 = '#fede00'
        self.accent_color_2 = '#000000'
        self.accent_color_3 = '#b29b00'
        self.accent_color_4 = '#edd002'
        self.anchor = 'w'
        self.relief = 'flat'
        self.cursor = 'hand2'
        
        self.order_dict = {}
        self.tmp_dict = {}
        self.prod_name_1 = '🛒 Burger\n• with vegetables •'
        self.prod_name_2 = '🛒 Pancake\n• with blueberries •'
        self.prod_name_3 = '🛒 Cupcake\n• chocolate •'
        self.prod_name_4 = '🛒 Apple Pie\n• with cinnamon •'
        self.prod_name_5 = '🛒 Brownie\n• chocolate •'
        self.prod_name_6 = '🛒 Cola\n• sugar-free •'
        
        self.show_home()
        self.root.mainloop()
        
        
    def show_background(self):
        self.bg = Label(self.root, background = self.accent_color_1)
        self.bg.place(width = 350, height = 500)
    
    
    def hover(self, btn, colorOnHover, colorOnLeave, colorfgOnHover, colorfgOnLeave):
        btn.bind("<Enter>", func = lambda i: btn.config(background = colorOnHover, foreground = colorfgOnHover))
        btn.bind("<Leave>", func = lambda i: btn.config(background = colorOnLeave, foreground = colorfgOnLeave))
        
        
    def show_home(self):
        self.show_background()
        self.logo = PhotoImage(file = 'assets\\logo.png')
        self.logo_widget = Label(self.root, image = self.logo, background = self.accent_color_1)
        self.logo_widget.place(x = 80, y = 5)
        self.decor = PhotoImage(file = 'assets\\decor.png')
        self.decor_widget = Label(self.root, image = self.decor, background = self.accent_color_1)
        self.decor_widget.place(x = 60, y = 250)
        self.show_menu()
    
    
    def show_menu(self):
        self.button_aboutus = Button(self.root, text = 'ABOUT US', command = self.show_about_us)
        self.button_aboutus.place(x = 20, y = 200, width = 80, height = 25)
        self.button_menu = Button(self.root, text = 'MENU', command = self.show_page_1)
        self.button_menu.place(x = 20, y = 225, width = 80, height = 25)
        self.button_recipes = Button(self.root, text = 'RECIPES', command = self.show_recipes)
        self.button_recipes.place(x = 20, y = 250, width = 80, height = 25)
        self.button_contacts = Button(self.root, text = 'CONTACTS', command = self.show_contacts)
        self.button_contacts.place(x = 20, y = 275, width = 80, height = 25)
        
        for i in (self.button_aboutus, self.button_menu, self.button_recipes, self.button_contacts):
            i.configure(
            background = self.accent_color_1,
            foreground = self.accent_color_2,
            font = self.accent_font_1,
            anchor = self.anchor,
            relief = self.relief,
            cursor = self.cursor,
            activebackground = self.accent_color_1,
            activeforeground = self.accent_color_3
            )
            self.hover(i, self.accent_color_4, self.accent_color_1, self.accent_color_3, self.accent_color_2)
    
    
    def show_page_1(self):
        self.page = 1
        self.show_background()
        self.show_close()
        self.burger = PhotoImage(file = 'assets\\burger.png')
        self.cupcake = PhotoImage(file = 'assets\\cupcake.png')
        self.pancake = PhotoImage(file = 'assets\\pancake.png')
        self.burgerwidget = Label(self.root, image = self.burger, background = self.accent_color_1)
        self.burgerwidget.place(x = 150, y = -30)
        self.pancakewidget = Label(self.root, image = self.pancake, background = self.accent_color_1)
        self.pancakewidget.place(x = -130, y = 160)
        self.cupcakewidget = Label(self.root, image = self.cupcake, background = self.accent_color_1)
        self.cupcakewidget.place(x = 200, y = 330)
        self.header_burgerwidget = Label(self.root, text = '', background = self.accent_color_1, font = self.accent_font_3, justify = LEFT, wraplength = 200)
        self.header_burgerwidget['text'] = 'Burger with Vegetables'
        self.text_burgerwidget = Label(self.root, text = '', background = self.accent_color_1, font = self.accent_font_1, justify = LEFT, wraplength = 140)
        self.text_burgerwidget['text'] = 'Enjoy deliciously simple craft Classic Burger with a juicy beef patty, lettuce, tomato, onions and pickles on a bun.'
        self.header_burgerwidget.place(x = 130, y = 5, width = 200)
        self.text_burgerwidget.place(x = 25, y = 50, width = 140)
        
        self.header_pancakewidget = Label(self.root, text = '', background = self.accent_color_1, font = self.accent_font_3, justify = LEFT, wraplength = 220)
        self.header_pancakewidget['text'] = 'Pancakes with Blueberries'
        self.text_pancakewidget = Label(self.root, text = '', background = self.accent_color_1, font = self.accent_font_1, justify = LEFT, wraplength = 100)
        self.text_pancakewidget['text'] = 'Thick and fluffy pancakes! Melt in your mouth, golden brown, and bursting with blueberries.'
        self.header_pancakewidget.place(x = 20, y = 173, width = 220)
        self.text_pancakewidget.place(x = 205, y = 215, width = 100)
        
        self.header_cupcakewidget = Label(self.root, text = '', background = self.accent_color_1, font = self.accent_font_3, justify = LEFT, wraplength = 165)
        self.header_cupcakewidget['text'] = 'Chocolate Cupcake'
        self.text_cupcakewidget = Label(self.root, text = '', background = self.accent_color_1, font = self.accent_font_1, justify = LEFT, wraplength = 160)
        self.text_cupcakewidget['text'] = 'These delicious cupcake has a chocolate centre once you get past the cream topping.'
        self.header_cupcakewidget.place(x = 160, y = 370, width = 165)
        self.text_cupcakewidget.place(x = 30, y = 405, width = 150)
        
        self.burgerwidget_output = Message(self.root, text = '0', background = self.accent_color_1, width = 5)
        self.burgerwidget_output.place(x = 192, y = 70)
        self.pancakewidget_output = Message(self.root, text = '0', background = self.accent_color_1, width = 5)
        self.pancakewidget_output.place(x = 150, y = 240)
        self.cupcakewidget_output = Message(self.root, text = '0', background = self.accent_color_1, width = 5)
        self.cupcakewidget_output.place(x = 208, y = 440)
        
        self.next_button = Button(self.root, text = '>', command = self.show_page_2)
        self.next_button.configure(
            background = self.accent_color_1,
            foreground = self.accent_color_2,
            font = self.accent_font_1,
            relief = self.relief,
            cursor = self.cursor,
            activebackground = self.accent_color_1,
            activeforeground = self.accent_color_3
            )
        self.hover(self.next_button, self.accent_color_4, self.accent_color_1, self.accent_color_3, self.accent_color_2)
        self.next_button.place(x = 305, y = 225, width = 25, height = 25)
        
        self.show_price()
        self.show_increase()
        self.show_decrease()
        self.check_selected_products()
    
    
    def show_page_2(self):
        self.page = 2
        self.show_background()
        self.show_close()
        self.applepie = PhotoImage(file = 'assets\\applepie.png')
        self.browniecake = PhotoImage(file = 'assets\\browniecake.png')
        self.cola = PhotoImage(file = 'assets\\cola.png')
        self.applepie_widget = Label(self.root, image = self.applepie, background = self.accent_color_1)
        self.applepie_widget.place(x = 130, y = -60)
        self.browniecake_widget = Label(self.root, image = self.browniecake, background = self.accent_color_1)
        self.browniecake_widget.place(x = -60, y = 160)
        self.cola_widget = Label(self.root, image = self.cola, background = self.accent_color_1)
        self.cola_widget.place(x = 180, y = 300)
        
        self.applepie_header = Label(self.root, text = '', background = self.accent_color_1, font = self.accent_font_3, justify = LEFT, wraplength = 200)
        self.applepie_header['text'] = 'Apple Pie with Cinnamon'
        self.applepie_text = Label(self.root, text = '', background = self.accent_color_1, font = self.accent_font_1, justify = LEFT, wraplength = 100)
        self.applepie_text['text'] = "This is absolutely the best homemade apple pie you'll ever taste!"
        self.applepie_header.place(x = 115, y = 5, width = 215)
        self.applepie_text.place(x = 20, y = 50, width = 100)
        
        self.browniecake_header = Label(self.root, text = '', background = self.accent_color_1, font = self.accent_font_3, justify = LEFT, wraplength = 200)
        self.browniecake_header['text'] = 'Chocolate Brownie Cake'
        self.browniecake_text = Label(self.root, text = '', background = self.accent_color_1, font = self.accent_font_1, justify = LEFT, wraplength = 95)
        self.browniecake_text['text'] = 'These delightful individual Chocolate Brownie cakes are the perfect mini treat.'
        self.browniecake_header.place(x = 20, y = 173, width = 200)
        self.browniecake_text.place(x = 205, y = 215, width = 95)
        
        self.cola_header = Label(self.root, text = '', background = self.accent_color_1, font = self.accent_font_3, justify = LEFT, wraplength = 150)
        self.cola_header['text'] = 'Refreshing Cola'
        self.cola_text = Label(self.root, text = '', background = self.accent_color_1, font = self.accent_font_1, justify = LEFT, wraplength = 160)
        self.cola_text['text'] = 'A sugar-free refreshing drink that looks and tastes like the classic Cola.'
        self.cola_header.place(x = 175, y = 370, width = 150)
        self.cola_text.place(x = 30, y = 405, width = 160)
        
        self.applepie_output = Message(self.root, text = '0', background = self.accent_color_1, width = 5)
        self.applepie_output.place(x = 192, y = 70)
        self.brownie_output = Message(self.root, text = '0', background = self.accent_color_1, width = 5)
        self.brownie_output.place(x = 150, y = 240)
        self.cola_output = Message(self.root, text = '0', background = self.accent_color_1, width = 5)
        self.cola_output.place(x = 208, y = 440)
        
        self.previous_button = Button(self.root, text = '<', command = self.show_page_1)
        self.previous_button.configure(
            background = self.accent_color_1,
            foreground = self.accent_color_2,
            font = self.accent_font_1,
            relief = self.relief,
            cursor = self.cursor,
            activebackground = self.accent_color_1,
            activeforeground = self.accent_color_3
            )
        self.hover(self.previous_button, self.accent_color_4, self.accent_color_1, self.accent_color_3, self.accent_color_2)
        self.previous_button.place(x = 20, y = 225, width = 25, height = 25)
        
        self.price_widget_4 = Label(self.applepie_widget, text = '$1.65', background = self.accent_color_1, font = self.accent_font_2, justify = LEFT, wraplength = 45)
        self.price_widget_5 = Label(self.browniecake_widget, text = '$1.99', background = self.accent_color_1, font = self.accent_font_2, justify = LEFT, wraplength = 45)
        self.price_widget_6 = Label(self.cola_widget, text = '$0.99', background = self.accent_color_1, font = self.accent_font_2, justify = LEFT, wraplength = 45)
        self.price_widget_4.place(x = 58, y = 100, width = 50, height = 25)
        self.price_widget_5.place(x = 180, y = 50, width = 50, height = 25)
        self.price_widget_6.place(x = 24, y = 110, width = 50, height = 25)
        self.show_increase()
        self.show_decrease()
        self.check_selected_products()
    
    
    def show_close(self):
        self.button = Button(self.root, text = 'x', command = self.close)
        self.button.configure(
            background = self.accent_color_1,
            foreground = self.accent_color_2,
            font = self.accent_font_1,
            relief = self.relief,
            cursor = self.cursor,
            activebackground = self.accent_color_1,
            activeforeground = self.accent_color_3
            )
        self.hover(self.button, self.accent_color_4, self.accent_color_1, self.accent_color_3, self.accent_color_2)
        self.button.place(x = 20, y = 20, width = 25, height = 25)

    
    def show_next(self, i):
        if i == 'burger':
            self.button = Button(self.root, text = '>', command = lambda:self.show_recipe('pancake'))
        elif i == "pancake":
            self.button = Button(self.root, text = '>', command = lambda:self.show_recipe('cupcake'))
        elif i == 'cupcake':
            self.button = Button(self.root, text = '>', command = lambda:self.show_recipe('applepie'))
        elif i == 'applepie':
            self.button = Button(self.root, text = '>', command = lambda:self.show_recipe('brownie'))
        else:
            self.button = Button(self.root, text = '>', command = lambda:self.show_recipe('burger'))
        self.button.configure(
            background = self.accent_color_1,
            foreground = self.accent_color_2,
            font = self.accent_font_1,
            relief = self.relief,
            cursor = self.cursor,
            activebackground = self.accent_color_1,
            activeforeground = self.accent_color_3
            )
        self.hover(self.button, self.accent_color_4, self.accent_color_1, self.accent_color_3, self.accent_color_2)
        self.button.place(x = 305, y = 225, width = 25, height = 25)
        
    
    def show_previous(self, i):
        if i == 'burger':
            self.button = Button(self.root, text = '<', command = lambda:self.show_recipe('brownie'))
        elif i == "brownie":
            self.button = Button(self.root, text = '<', command = lambda:self.show_recipe('applepie'))
        elif i == 'applepie':
            self.button = Button(self.root, text = '<', command = lambda:self.show_recipe('cupcake'))
        elif i == 'cupcake':
            self.button = Button(self.root, text = '<', command = lambda:self.show_recipe('pancake'))
        else:
            self.button = Button(self.root, text = '<', command = lambda:self.show_recipe('burger'))
        self.button.configure(
            background = self.accent_color_1,
            foreground = self.accent_color_2,
            font = self.accent_font_1,
            relief = self.relief,
            cursor = self.cursor,
            activebackground = self.accent_color_1,
            activeforeground = self.accent_color_3
            )
        self.hover(self.button, self.accent_color_4, self.accent_color_1, self.accent_color_3, self.accent_color_2)
        self.button.place(x = 20, y = 225, width = 25, height = 25)
        
    
    def show_back(self):
        self.button = Button(self.root, text = '<', command = self.show_recipes)
        self.button.configure(
            background = self.accent_color_1,
            foreground = self.accent_color_2,
            font = self.accent_font_1,
            relief = self.relief,
            cursor = self.cursor,
            activebackground = self.accent_color_1,
            activeforeground = self.accent_color_3
            )
        self.hover(self.button, self.accent_color_4, self.accent_color_1, self.accent_color_3, self.accent_color_2)
        self.button.place(x = 45, y = 20, width = 25, height = 25)
    
    
    def show_price(self):
        self.price_widget_1 = Label(self.burgerwidget, text = '$2.50', background = self.accent_color_1, font = self.accent_font_2, justify = LEFT, anchor = 'e', wraplength = 45)
        self.price_widget_2 = Label(self.pancakewidget, text = '$6.75', background = self.accent_color_1, font = self.accent_font_2, justify = LEFT, wraplength = 45)
        self.price_widget_3 = Label(self.cupcakewidget, text = '$2.15', background = self.accent_color_1, font = self.accent_font_2, justify = LEFT, wraplength = 45)
        self.price_widget_1.place(x = 5, y = 70, width = 83, height = 25)
        self.price_widget_2.place(x = 250, y = 50, width = 50, height = 25)
        self.price_widget_3.place(x = 4, y = 80, width = 50, height = 25)
    
    
    def show_basket(self):
        self.basket_button = Button(self.root, text = '🛒', command = self.get_order)
        self.basket_button.place(x = 45, y = 20, width = 25, height = 25)
                    
        self.basket_button.configure(
            background = self.accent_color_1,
            foreground = self.accent_color_2,
            font = self.accent_font_1,
            relief = self.relief,
            cursor = self.cursor,
            activebackground = self.accent_color_1,
            activeforeground = self.accent_color_3
            )
        self.hover(self.basket_button, self.accent_color_4, self.accent_color_1, self.accent_color_3, self.accent_color_2)
        
        
    def show_increase(self):
        self.increase_button_1 = Button(self.root, text = '+', command = lambda:self.increase(1, 'increase_button_1'))
        self.increase_button_2 = Button(self.root, text = '+', command = lambda:self.increase(1, 'increase_button_2'))
        self.increase_button_3 = Button(self.root, text = '+', command = lambda:self.increase(1, 'increase_button_3'))
        for i in (self.increase_button_1, self.increase_button_2, self.increase_button_3):
            i.configure(
            background = self.accent_color_1,
            foreground = self.accent_color_2,
            font = self.accent_font_1,
            relief = self.relief,
            cursor = self.cursor,
            activebackground = self.accent_color_1,
            activeforeground = self.accent_color_3
            )
            self.hover(i, self.accent_color_4, self.accent_color_1, self.accent_color_3, self.accent_color_2)
        self.increase_button_1.place(x = 215, y = 70, width = 25, height = 25)
        self.increase_button_2.place(x = 173, y = 240, width = 25, height = 25)
        self.increase_button_3.place(x = 231, y = 440, width = 25, height = 25)
    
    
    def show_decrease(self):
        self.decrease_button_1 = Button(self.root, text = '-', command = lambda:self.decrease(1, 'decrease_button_1'))
        self.decrease_button_2 = Button(self.root, text = '-', command = lambda:self.decrease(1, 'decrease_button_2'))
        self.decrease_button_3 = Button(self.root, text = '-', command = lambda:self.decrease(1, 'decrease_button_3'))
        for i in (self.decrease_button_1, self.decrease_button_2, self.decrease_button_3):
            i.configure(
            background = self.accent_color_1,
            foreground = self.accent_color_2,
            font = self.accent_font_1,
            relief = self.relief,
            cursor = self.cursor,
            activebackground = self.accent_color_1,
            activeforeground = self.accent_color_3
            )
            self.hover(i, self.accent_color_4, self.accent_color_1, self.accent_color_3, self.accent_color_2)
        self.decrease_button_1.place(x = 164, y = 70, width = 25, height = 25)
        self.decrease_button_2.place(x = 122, y = 240, width = 25, height = 25)
        self.decrease_button_3.place(x = 180, y = 440, width = 25, height = 25)

            
    def increase(self, i, y):
        self.val = int(i)
        if self.page == 1:
            if y == 'increase_button_1' and int(self.burgerwidget_output['text']) < 9:
                self.val += int(self.burgerwidget_output['text'])
                self.burgerwidget_output['text'] = str(self.val)
            elif y == 'increase_button_2' and int(self.pancakewidget_output['text']) < 9:
                self.val += int(self.pancakewidget_output['text'])
                self.pancakewidget_output['text'] = str(self.val)
            elif y == 'increase_button_3' and int(self.cupcakewidget_output['text']) < 9:
                self.val += int(self.cupcakewidget_output['text'])
                self.cupcakewidget_output['text'] = str(self.val)
            self.show_basket()
        else:
            if y == 'increase_button_1' and int(self.applepie_output['text']) < 9:
                self.val += int(self.applepie_output['text'])
                self.applepie_output['text'] = str(self.val)
            elif y == 'increase_button_2' and int(self.brownie_output['text']) < 9:
                self.val += int(self.brownie_output['text'])
                self.brownie_output['text'] = str(self.val)
            elif y == 'increase_button_3' and int(self.cola_output['text']) < 9:
                self.val += int(self.cola_output['text'])
                self.cola_output['text'] = str(self.val)
            self.show_basket()
    
            
    def decrease(self, i, y):
        self.val = int(i)
        if self.page == 1:
            if y == 'decrease_button_1' and int(self.burgerwidget_output['text']) != 0:
                x = int(self.burgerwidget_output['text'])
                x -= self.val
                self.burgerwidget_output['text'] = str(x)
            elif y == 'decrease_button_2' and int(self.pancakewidget_output['text']) != 0:
                x = int(self.pancakewidget_output['text'])
                x -= self.val
                self.pancakewidget_output['text'] = str(x)
            elif y == 'decrease_button_3' and int(self.cupcakewidget_output['text']) != 0:
                x = int(self.cupcakewidget_output['text'])
                x -= self.val
                self.cupcakewidget_output['text'] = str(x)
        else:
            if y == 'decrease_button_1' and int(self.applepie_output['text']) != 0:
                x = int(self.applepie_output['text'])
                x -= self.val
                self.applepie_output['text'] = str(x)
            elif y == 'decrease_button_2' and int(self.brownie_output['text']) != 0:
                x = int(self.brownie_output['text'])
                x -= self.val
                self.brownie_output['text'] = str(x)
            elif y == 'decrease_button_3' and int(self.cola_output['text']) != 0:
                x = int(self.cola_output['text'])
                x -= self.val
                self.cola_output['text'] = str(x)
        
    
    def show_about_us(self):
        self.show_background()
        self.show_close()
        self.decor = PhotoImage(file = 'assets\\decor_about_us.png')
        self.decor_widget = Label(self.root, image = self.decor, background = self.accent_color_1)
        self.decor_widget.place(x = 60, y = 250)
        self.text_header = Label(self.root, text = 'Welcome to Burger Cafe!\n\n', background = self.accent_color_1, font = self.accent_font_3, justify = LEFT, wraplength = 260)
        self.text_widget = Label(self.root, text = '', background = self.accent_color_1, font = self.accent_font_1, justify = LEFT, wraplength = 260)
        self.text_widget['text'] = 'Burger Cafe is a family-friendly cafe that serves the best burgers with refreshing Cola. In addition you will find here a lot of delighting goodies: Apple Pie, Pancakes, Chocolate Brownie and Chocolate Cupcakes.\n\nAll of our products are prepared with the finest and freshest ingredients!'
        self.text_header.place(x = 45, y = 50, width = 260)
        self.text_widget.place(x = 45, y = 100, width = 260)
        
    
    def show_recipes(self):
        self.show_background()
        self.show_close()
        self.decor = PhotoImage(file = 'assets\\decor_recipes.png')
        self.decor_widget = Label(self.root, image = self.decor, background = self.accent_color_1)
        self.decor_widget.place(x = 60, y = 250)
        self.text_header = Label(self.root, text = 'Recipes.\n\n', background = self.accent_color_1, font = self.accent_font_3, justify = LEFT, wraplength = 260)
        self.recipe_1 = Button(self.root, text = 'BURGERS WITH VEGETABLES', command = lambda:self.show_recipe('burger'))
        self.recipe_2 = Button(self.root, text = 'PANCAKE WITH BLUEBERRIES', command = lambda:self.show_recipe('pancake'))
        self.recipe_3 = Button(self.root, text = 'CHOCOLATE CUPCAKES', command = lambda:self.show_recipe('cupcake'))
        self.recipe_4 = Button(self.root, text = 'APPLE PIE WITH CINNAMON', command = lambda:self.show_recipe('applepie'))
        self.recipe_5 = Button(self.root, text = 'CHOCOLATE BROWNIE CAKE', command = lambda:self.show_recipe('brownie'))
        
        for i in (self.recipe_1, self.recipe_2, self.recipe_3, self.recipe_4, self.recipe_5):
            i.configure(
            background = self.accent_color_1,
            foreground = self.accent_color_2,
            font = self.accent_font_1,
            anchor = self.anchor,
            relief = self.relief,
            cursor = self.cursor,
            activebackground = self.accent_color_1,
            activeforeground = self.accent_color_3
            )
            self.hover(i, self.accent_color_4, self.accent_color_1, self.accent_color_3, self.accent_color_2)
        self.text_header.place(x = 45, y = 50, width = 260)
        self.recipe_1.place(x = 70, y = 100, width = 205, height = 25)
        self.recipe_2.place(x = 70, y = 125, width = 205, height = 25)
        self.recipe_3.place(x = 70, y = 150, width = 205, height = 25)
        self.recipe_4.place(x = 70, y = 175, width = 205, height = 25)
        self.recipe_5.place(x = 70, y = 200, width = 205, height = 25)

    
    def show_recipe(self, i):
        self.show_background()  
        self.show_close()
        self.show_next(i)
        self.show_previous(i)
        self.text_widget = Label(self.root, text = '', background = self.accent_color_1, font = self.accent_font_1, justify = LEFT, wraplength = 260)
        self.header_widget = Label(self.root, text = '', background = self.accent_color_1, font = self.accent_font_3, justify = LEFT, wraplength = 260)
        if i == 'burger':
            self.header_widget['text'] = 'Burger with Vegetables'
            self.text_widget['text'] = 'Ingredients:\n* 1 small onion, diced,* 500g good-quality beef mince,* 1 egg,* 1 tbsp vegetable oil,* 4 burger buns,* all or any of the following to serve: sliced tomato, beetroot, horseradish sauce, mayonnaise, ketchup, handful iceberg lettuce, rocket, watercress\n\nMethod:\nTip 500g beef mince into a bowl with 1 small diced onion and 1 egg, then mix. Divide the mixture into four. Roll the mixture into balls and squeeze down to flatten into patties. Put on a plate, cover with cling film and leave in the fridge to firm up for at least 30 mins. Heat the barbecue to medium hot. Lightly brush one side of each burger with vegetable oil. Place the burgers, oil-side down, on the barbecue. Cook for 5 mins until the meat is lightly charred. Oil the other side, then turn over using tongs. Slice four burger buns in half. Place, cut-side down, on the barbecue rack and toast for 1 min until they are lightly charred. Place a burger inside each bun.'
        elif i == 'pancake':
            self.header_widget['text'] = 'Pancakes with Blueberries'
            self.text_widget['text'] = 'Ingredients:\n* 200g self-raising flour,* 1 tsp baking powder,* 1 egg,* 300ml milk,* knob butter,* 150g pack blueberry,* sunflower oil or a little butter for cooking,* golden or maple syrup\n\nMethod:\nMix together 200g self-raising flour, 1 tsp baking powder and a pinch of salt in a large bowl. Beat 1 egg with 300ml milk, make a well in the centre of the dry ingredients and whisk in the milk to make a thick smooth batter. Beat in a knob of melted butter, and stir in half of the 150g pack of blueberries. Heat a teaspoon of sunflower oil or small knob of butter in a frying pan. Drop a large tablespoonful of the batter per pancake into the pan to make pancakes about 7.5cm across. Cook for about 3 minutes over a medium heat, then turn and cook another 2-3 minutes until golden. Cover with kitchen paper to keep warm while you use up the rest of the batter. Serve with golden or maple syrup and the rest of the blueberries.'
        elif i == 'cupcake':
            self.header_widget['text'] = 'Chocolate Cupcakes'
            self.text_widget['text'] = 'Ingredients:\n* 110g softened butter,* 110g golden caster sugar,* 2 large eggs,* ½ tsp vanilla extract,* 110g self-raising flour,* 150g softened butter,* 300g icing sugar,* 1 tsp vanilla extract,* 3 tbsp milk\n\nMethod:\nHeat oven to 180C/160C fan/gas and fill a 12 cupcake tray with cases. Using a whisk beat 110g softened butter and 110g golden caster sugar together until pale and fluffy then whisk in 2 large eggs, one at a time, scraping down the sides of the bowl after each addition. Add ½ tsp vanilla extract, 110g self-raising flour and a pinch of salt, whisk until just combined then spoon the mixture into the cupcake cases. Bake for 15 mins until golden brown and a skewer inserted into the middle of each cake comes out clean. To make the buttercream, whisk 150g softened butter until super soft then add 300g icing sugar, 1 tsp vanilla extract and a pinch of salt. Whisk together until smooth then beat in 3 tbsp milk.'
        elif i == 'applepie':
            self.header_widget['text'] = 'Apple Pie with Cinnamon'
            self.text_widget['text'] = 'Ingredients:\n* 1kg apples,* 200g golden sugar,* ½ tsp cinnamon,* 3 tbsp flour,* 225g butter,* 2 eggs,* 350g flour,* softly whipped cream\n\nMethod:\nPeel and slice the apples and lay on the baking sheet with a layer of paper towel. For the pastry, beat the butter and sugar. Break in a whole egg and a yolk. Beat together for under 1 min. Work in the flour with a spoon until it’s beginning to clump up. Work the dough into a ball and chill for 45 mins. Mix the 140g sugar, the cinnamon and flour for the filling in a bowl. Heat the oven to 190C/fan 170C/gas. Beat the egg white. Cut off a third of the pastry, keep it and roll out the rest. Use this to line a pie tin 4cm deep. Roll the remaining third to a circle about 28cm in diameter. Tip the apples into the bowl with the cinnamon-sugar mix. Pile high into the tin, lay the pastry lid over the apples. Brush it all with the egg white and sprinkle with caster sugar. Bake for 40-45 mins, until golden.'
        else:
            self.header_widget['text'] = 'Chocolate Brownie Cake'
            self.text_widget['text'] = 'Ingredients:\n* 100g butter,* 125g caster sugar,* 75g brown sugar,* 125g chocolate,* 1 tbsp golden syrup,* 2 eggs,* 1 tsp vanilla extract,* 100g flour,* ½ tsp baking powder,* 2 tbsp cocoa powder\n\nMethod:\nHeat oven to 180C/fan 160C/gas. Grease and line a 20cm cake tin. Place the butter, caster sugar, brown sugar, chocolate and golden syrup in the pan and melt gently on a low heat until it is smooth and lump-free. Remove the pan from the heat. Break the eggs into the bowl and whisk with the fork until light and frothy. 5 Add the eggs, vanilla extract or essence, flour, baking powder and cocoa powder to the chocolate mixture and mix thoroughly. Put the mixture into the greased and lined cake tin and place on the middle shelf of the oven. Bake for 25-30 mins. Remove and allow to cool for 20-30 mins before cutting into wedges and serving. Serve with cream or ice cream and plenty of fresh fruit.'
        self.header_widget.place(x = 45, y = 20, width = 260)
        self.text_widget.place(x = 45, y = 65, width = 260)
        self.show_back()
        
    
    def show_contacts(self):
        self.show_background()
        self.show_close()
        self.decor = PhotoImage(file = 'assets\\decor_contacts.png')
        self.decor_widget = Label(self.root, image = self.decor, background = self.accent_color_1)
        self.decor_widget.place(x = 60, y = 250)
        self.text_header = Label(self.root, text = 'Schedule & Contacts.\n\n', background = self.accent_color_1, font = self.accent_font_3, justify = LEFT, wraplength = 260)
        self.text_widget = Label(self.root, text = '', background = self.accent_color_1, font = self.accent_font_1, justify = LEFT, wraplength = 260)
        self.text_widget['text'] = 'Burger Cafe is open 7 days a week & offers delivery.'
        self.text_header.place(x = 45, y = 50, width = 260)
        self.text_widget.place(x = 45, y = 100, width = 260)
    
    
    def get_order(self):
        if self.page == 1:
            self.prods_dict_page_1 = {f'{self.prod_name_1}': f'{self.burgerwidget_output["text"]}', f'{self.prod_name_2}': f'{self.pancakewidget_output["text"]}', f'{self.prod_name_3}': f'{self.cupcakewidget_output["text"]}'}
            for key in self.prods_dict_page_1:
                self.tmp_dict[key] = self.prods_dict_page_1[key]
            self.order_dict.update(self.tmp_dict)
        else:
            self.prods_dict_page_2 = {f'{self.prod_name_4}': f'{self.applepie_output["text"]}', f'{self.prod_name_5}': f'{self.brownie_output["text"]}', f'{self.prod_name_6}': f'{self.cola_output["text"]}'}
            for key in self.prods_dict_page_2:
                self.tmp_dict[key] = self.prods_dict_page_2[key]
            self.order_dict.update(self.tmp_dict)
        self.bill()
    
    
    def check_selected_products(self):
        if self.page == 1:
            try:
                self.prods_dict_page_2 = {f'{self.prod_name_4}': f'{self.applepie_output["text"]}', f'{self.prod_name_5}': f'{self.brownie_output["text"]}', f'{self.prod_name_6}': f'{self.cola_output["text"]}'}
                for key in self.prods_dict_page_2:
                    self.tmp_dict[key] = self.prods_dict_page_2[key]
                self.order_dict.update(self.tmp_dict)
            except AttributeError:
                pass
            
            try:
                self.burgerwidget_output["text"] = self.order_dict[f'{self.prod_name_1}']
                self.pancakewidget_output["text"] = self.order_dict[f'{self.prod_name_2}']
                self.cupcakewidget_output["text"] = self.order_dict[f'{self.prod_name_3}']
            except KeyError:
                pass
            
        else:
            self.prods_dict_page_1 = {f'{self.prod_name_1}': f'{self.burgerwidget_output["text"]}', f'{self.prod_name_2}': f'{self.pancakewidget_output["text"]}', f'{self.prod_name_3}': f'{self.cupcakewidget_output["text"]}'}
            for key in self.prods_dict_page_1:
                self.tmp_dict[key] = self.prods_dict_page_1[key]
                self.order_dict.update(self.tmp_dict)
            
            try:
                self.applepie_output['text'] = self.order_dict[f'{self.prod_name_4}']
                self.brownie_output['text'] = self.order_dict[f'{self.prod_name_5}']
                self.cola_output['text'] = self.order_dict[f'{self.prod_name_6}']
            except KeyError:
                pass
        self.show_basket()
        
        
    def bill(self):
        self.show_page_2()
        self.show_background()
        self.show_close()
        self.decor = PhotoImage(file = 'assets\\decor_about_us.png')
        self.decor_widget = Label(self.root, image = self.decor, background = self.accent_color_1)
        self.decor_widget.place(x = 60, y = 250)
        self.bill_prods_widget = Label(self.root, text = '', background = self.accent_color_1, font = self.accent_font_1, justify = LEFT, wraplength = 110)
        self.bill_cost_widget = Label(self.root, text = '', background = self.accent_color_1, font = self.accent_font_1, justify = RIGHT, wraplength = 200)
        self.bill_total_name_widget = Label(self.root, text = '', background = self.accent_color_1, font = self.accent_font_1, justify = LEFT, wraplength = 90)
        self.bill_total_cost_widget = Label(self.root, text = '', background = self.accent_color_1, font = self.accent_font_2, justify = LEFT, wraplength = 90)
        
        self.prices_dict = {f'{self.prod_name_1}': f'{self.price_widget_1["text"]}', f'{self.prod_name_2}': f'{self.price_widget_2["text"]}', f'{self.prod_name_3}': f'{self.price_widget_3["text"]}', f'{self.prod_name_4}': f'{self.price_widget_4["text"]}', f'{self.prod_name_5}': f'{self.price_widget_5["text"]}', f'{self.prod_name_6}': f'{self.price_widget_6["text"]}'}
        self.dots, self.tmp_list, self.prods_list, self.cost_list = [], [], [], []
        self.dots_length = 23
        self.to_pay_per_position_list = []
        
        for i in self.order_dict:
            if self.order_dict[i] != "0":
                self.tmp_list.append(str(f'{i}: {self.order_dict[i]}'))

        for i in range(0, len(self.tmp_list)):
            for y in range(0, self.dots_length):
                self.dots.append('.')
                name = self.tmp_list[i].split(': ')[0]
                quantity = self.tmp_list[i].split(': ')[-1]
                price = self.prices_dict[name]
                to_pay_per_position = (int(quantity) * float(price.split('$')[-1]))
                to_pay_per_position_formated = "{:.2f}".format(to_pay_per_position)
            self.prods_list.append(name)
            self.to_pay_per_position_list.append(to_pay_per_position)
            
            if name in self.prices_dict:
                self.cost_list.append(f"{''.join(i for i in self.dots)} {quantity}x {price}\nTotal: ${to_pay_per_position_formated}")
                self.dots = []
        
        self.total_cost = 0
        for i in self.to_pay_per_position_list:
            i += self.total_cost
            self.total_cost = i
        self.total_cost_formated = "{:.2f}".format(self.total_cost)
          
        self.bill_prods_widget['text'] = '\n'.join(i for i in self.prods_list)
        self.bill_prods_widget.place(x = 30, y = 50, width = 130)
        
        self.bill_cost_widget['text'] = '\n'.join(i for i in self.cost_list)
        self.bill_cost_widget.place(x = 155, y = 50, width = 160)
        
        self.bill_total_name_widget['text'] = 'Total:\n'
        self.bill_total_name_widget.place(x = 22, y = 320, width = 90)
        
        self.bill_total_cost_widget['text'] = f'${self.total_cost_formated}'
        self.bill_total_cost_widget.place(x = 45, y = 340, width = 50)
        
        
    def close(self):
        try:
            for i in (self.decor_widget,self.text_widget,self.recipe_1,self.recipe_2,self.recipe_3,self.button):
                i.destroy()
        except AttributeError:
            pass
        
        self.order_dict, self.tmp_dict = {}, {}
        try:
            for i in (self.burgerwidget_output,self.pancakewidget_output,self.cupcakewidget_output,self.applepie_output,self.brownie_output,self.cola_output):
                i['text'] = "0"
        except AttributeError:
            pass
        
        self.show_home()

if __name__ == '__main__':
    App()