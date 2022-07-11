from tkinter import *
from tkinter import font
import pyglet
import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\burgercafe-menu\\')

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
        self.bold = ('TkMenuFont',10, 'bold')
        self.bgcolor = '#fede00'
        self.fgcolor = '#000000'
        self.menu_fgcolor = '#b29b00'
        self.showMainPage()
        self.root.mainloop()
        
        
    def showMainPage(self):
        self.showBackground()
        self.logo = PhotoImage(file = 'assets\\logo.png')
        self.logowidget = Label(self.root, image = self.logo, background = self.bgcolor)
        self.logowidget.place(x = 80, y = 5)
        self.decor = PhotoImage(file = 'assets\\decor.png')
        self.decorwidget = Label(self.root, image = self.decor, background = self.bgcolor)
        self.decorwidget.place(x = 60, y = 250)
        self.showMenu()
        
        self.button = Button(self.root, text = '🛒')
        self.button.configure(
            background = self.bgcolor,
            foreground = self.fgcolor,
            font = self.font,
            relief = 'flat',
            cursor = 'hand2',
            activebackground = self.bgcolor,
            activeforeground = self.menu_fgcolor
            )
        self.hover(self.button, '#edd002','#fede00', self.menu_fgcolor, self.fgcolor)
        self.button.place(x = 30, y = 30, width = 25, height = 25)
        
    
    
    def showMenu(self):
        self.button_aboutus = Button(self.root, text = 'ABOUT US', command = self.showAboutUsPage)
        self.button_aboutus.place(x = 30, y = 200, width = 80)
        self.button_menu = Button(self.root, text = 'MENU', command = self.showMenuPage)
        self.button_menu.place(x = 30, y = 225, width = 80)
        self.button_recipes = Button(self.root, text = 'RECIPES', command = self.showRecipesPage)
        self.button_recipes.place(x = 30, y = 250, width = 80)
        self.button_contacts = Button(self.root, text = 'CONTACTS', command = self.showContactsPage)
        self.button_contacts.place(x = 30, y = 275, width = 80)
        
        for i in (self.button_aboutus, self.button_menu, self.button_recipes, self.button_contacts):
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
            self.hover(i,'#edd002','#fede00', self.menu_fgcolor, self.fgcolor)
    

    def hover(self, btn, colorOnHover, colorOnLeave, colorfgOnHover, colorfgOnLeave):
        btn.bind("<Enter>", func = lambda i: btn.config(background = colorOnHover, foreground = colorfgOnHover))
        btn.bind("<Leave>", func = lambda i: btn.config(background = colorOnLeave, foreground = colorfgOnLeave))
        
    
    def showBackground(self):
        self.bg = Label(self.root, background = '#fede00')
        self.bg.place(width = 350, height = 500)
    
    
    def showCloseButton(self):
        self.button = Button(self.root, text = 'x', command = self.closePage)
        self.button.configure(
            background = self.bgcolor,
            foreground = self.fgcolor,
            font = self.font,
            relief = 'flat',
            cursor = 'hand2',
            activebackground = self.bgcolor,
            activeforeground = self.menu_fgcolor
            )
        self.hover(self.button, '#edd002','#fede00', self.menu_fgcolor, self.fgcolor)
        self.button.place(x = 10, y = 10, width = 25, height = 25)
    
    
    def showBackButton(self):
        self.button = Button(self.root, text = '<<', command = self.showRecipesPage)
        self.button.configure(
            background = self.bgcolor,
            foreground = self.fgcolor,
            font = self.font,
            relief = 'flat',
            cursor = 'hand2',
            activebackground = self.bgcolor,
            activeforeground = self.menu_fgcolor
            )
        self.hover(self.button, '#edd002','#fede00', self.menu_fgcolor, self.fgcolor)
        self.button.place(x = 10, y = 35, width = 25, height = 25)

    
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
        self.hover(self.button, '#edd002','#fede00', self.menu_fgcolor, self.fgcolor)
        self.button.place(x = 315, y = 225, width = 25, height = 25)
        
    
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
        self.hover(self.button, '#edd002','#fede00', self.menu_fgcolor, self.fgcolor)
        self.button.place(x = 5, y = 225, width = 25, height = 25)
    
    
    def showMenuPage(self):
        self.showBackground()
        self.showCloseButton()
        self.burger = PhotoImage(file = 'assets\\burger.png')
        self.cupcake = PhotoImage(file = 'assets\\cupcake.png')
        self.pancake = PhotoImage(file = 'assets\\pancake.png')
        self.burgerwidget = Label(self.root, image = self.burger, background = self.bgcolor)
        self.burgerwidget.place(x = 150, y = -30)
        self.pancakewidget = Label(self.root, image = self.pancake, background = self.bgcolor)
        self.pancakewidget.place(x = -130, y = 160)
        self.cupcakewidget = Label(self.root, image = self.cupcake, background = self.bgcolor)
        self.cupcakewidget.place(x = 200, y = 300)
        self.boldwidget1 = Label(self.burgerwidget, text = '', background = '#fede00', font = self.bold, justify = LEFT, wraplength = 150)
        self.boldwidget1['text'] = 'Burger with Vegetables'
        self.textwidget1 = Label(self.root, text = '', background = '#fede00', font = self.font, justify = LEFT, wraplength = 140)
        self.textwidget1['text'] = 'Enjoy deliciously simple craft Classic Burger with a juicy beef patty, lettuce, tomato, onions and pickles on a bun.'
        self.boldwidget1.place(x = 0, y = 50, width = 160)
        self.textwidget1.place(x = 25, y = 40, width = 140)
        
        self.boldwidget2 = Label(self.pancakewidget, text = '', background = '#fede00', font = self.bold, justify = LEFT, wraplength = 170)
        self.boldwidget2['text'] = 'Pancakes with Blueberries'
        self.textwidget2 = Label(self.root, text = '', background = '#fede00', font = self.font, justify = LEFT, wraplength = 120)
        self.textwidget2['text'] = 'Super thick and fluffy pancakes! Melt in your mouth, golden brown, and bursting with blueberries.'
        self.boldwidget2.place(x = 150, y = 20, width = 180)
        self.textwidget2.place(x = 195, y = 200, width = 150)
        
        self.boldwidget3 = Label(self.cupcakewidget, text = '', background = '#fede00', font = self.bold, justify = LEFT, wraplength = 130)
        self.boldwidget3['text'] = 'Chocolate Cupcake'
        self.textwidget3 = Label(self.root, text = '', background = '#fede00', font = self.font, justify = LEFT, wraplength = 160)
        self.textwidget3['text'] = 'These delicious cupcake has a chocolate centre once you get past the cream topping.'
        self.boldwidget3.place(x = 0, y = 80, width = 130)
        self.textwidget3.place(x = 25, y = 405, width = 150)
        
        self.button1 = Button(self.burgerwidget, text = '🛒')
        self.button2 = Button(self.pancakewidget, text = '🛒')
        self.button3 = Button(self.cupcakewidget, text = '🛒')
        for i in (self.button1, self.button2, self.button3):
            i.configure(
            background = self.bgcolor,
            foreground = self.fgcolor,
            font = self.font,
            relief = 'flat',
            cursor = 'hand2',
            activebackground = self.bgcolor,
            activeforeground = self.menu_fgcolor
            )
            self.hover(i, '#edd002','#fede00', self.menu_fgcolor, self.fgcolor)
        self.button1.place(x = 20, y = 145, width = 25, height = 25)
        self.button2.place(x = 300, y = 110, width = 25, height = 25)
        self.button3.place(x = 0, y = 145, width = 25, height = 25)
        
        
    def showAboutUsPage(self):
        self.showBackground()
        self.showCloseButton()
        self.decor = PhotoImage(file = 'assets\\decor_about_us.png')
        self.decorwidget = Label(self.root, image = self.decor, background = self.bgcolor)
        self.decorwidget.place(x = 60, y = 250)
        self.textwidget = Label(self.root, text = '', background = '#fede00', font = self.font, justify = LEFT, wraplength = 260)
        self.textwidget['text'] = 'Welcome to Burger Cafe!\n\nHome of the best burgers. Located in the beautiful city, Burger Cafe is a family-friendly cafe that serves the best burgers, pancakes and cupcakes.\n\nAll of our products are prepared with the finest and freshest ingredients!'
        self.textwidget.place(x = 45, y = 50, width = 260)
        
    
    def showRecipesPage(self):
        self.showBackground()
        self.showCloseButton()
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
            self.hover(i,'#edd002','#fede00', self.menu_fgcolor, self.fgcolor)
        self.recipe1.place(x = 45, y = 50, width = 205)
        self.recipe2.place(x = 45, y = 80, width = 205)
        self.recipe3.place(x = 45, y = 110, width = 205)
      
    
    def showRecipe(self, i):
        self.showBackground()
        self.showCloseButton()
        self.showBackButton()
        self.showNext(i)
        self.showPrevious(i)
        self.textwidget = Label(self.root, text = '', background = '#fede00', font = self.font, justify = LEFT, wraplength = 260)
        self.boldtwidget = Label(self.root, text = '', background = '#fede00', font = self.bold, justify = LEFT, wraplength = 260)
        if i == 'burger':
            self.boldtwidget['text'] = 'Burger with Vegetables'
            self.textwidget['text'] = 'Ingredients:\n* 1 small onion, diced,* 500g good-quality beef mince,* 1 egg,* 1 tbsp vegetable oil,* 4 burger buns,* all or any of the following to serve: sliced tomato, beetroot, horseradish sauce, mayonnaise, ketchup, handful iceberg lettuce, rocket, watercress\n\nMethod:\nTip 500g beef mince into a bowl with 1 small diced onion and 1 egg, then mix. Divide the mixture into four. Roll the mixture into balls and squeeze down to flatten into patties. Put on a plate, cover with cling film and leave in the fridge to firm up for at least 30 mins. Heat the barbecue to medium hot. Lightly brush one side of each burger with vegetable oil. Place the burgers, oil-side down, on the barbecue. Cook for 5 mins until the meat is lightly charred. Oil the other side, then turn over using tongs. Slice four burger buns in half. Place, cut-side down, on the barbecue rack and toast for 1 min until they are lightly charred. Place a burger inside each bun.'
        elif i == 'pancake':
            self.boldtwidget['text'] = 'Pancakes with Blueberries'
            self.textwidget['text'] = 'Ingredients:\n* 200g self-raising flour,* 1 tsp baking powder,* 1 egg,* 300ml milk,* knob butter,* 150g pack blueberry,* sunflower oil or a little butter for cooking,* golden or maple syrup\n\nMethod:\nMix together 200g self-raising flour, 1 tsp baking powder and a pinch of salt in a large bowl. Beat 1 egg with 300ml milk, make a well in the centre of the dry ingredients and whisk in the milk to make a thick smooth batter. Beat in a knob of melted butter, and stir in half of the 150g pack of blueberries. Heat a teaspoon of sunflower oil or small knob of butter in a frying pan. Drop a large tablespoonful of the batter per pancake into the pan to make pancakes about 7.5cm across. Cook for about 3 minutes over a medium heat, then turn and cook another 2-3 minutes until golden. Cover with kitchen paper to keep warm while you use up the rest of the batter. Serve with golden or maple syrup and the rest of the blueberries.'
        else:
            self.boldtwidget['text'] = 'Chocolate Cupcakes'
            self.textwidget['text'] = 'Ingredients:\n* 110g softened butter,* 110g golden caster sugar,* 2 large eggs,* ½ tsp vanilla extract,* 110g self-raising flour,* 150g softened butter,* 300g icing sugar,* 1 tsp vanilla extract,* 3 tbsp milk\n\nMethod:\nHeat oven to 180C/160C fan/gas and fill a 12 cupcake tray with cases. Using a whisk beat 110g softened butter and 110g golden caster sugar together until pale and fluffy then whisk in 2 large eggs, one at a time, scraping down the sides of the bowl after each addition. Add ½ tsp vanilla extract, 110g self-raising flour and a pinch of salt, whisk until just combined then spoon the mixture into the cupcake cases. Bake for 15 mins until golden brown and a skewer inserted into the middle of each cake comes out clean. To make the buttercream, whisk 150g softened butter until super soft then add 300g icing sugar, 1 tsp vanilla extract and a pinch of salt. Whisk together until smooth then beat in 3 tbsp milk.'
        self.boldtwidget.place(x = 45, y = 25, width = 260)
        self.textwidget.place(x = 45, y = 50, width = 260)
        
    
    def showContactsPage(self):
        self.showBackground()
        self.showCloseButton()
        self.decor = PhotoImage(file = 'assets\\decor_contacts.png')
        self.decorwidget = Label(self.root, image = self.decor, background = self.bgcolor)
        self.decorwidget.place(x = 60, y = 250)
        self.textwidget = Label(self.root, text = '', background = self.bgcolor, font = self.font, justify = LEFT, wraplength = 260)
        self.textwidget['text'] = 'Schedule & Contacts.\n\nBurger Cafe is open 7 days a week & offers delivery.'
        self.textwidget.place(x = 45, y = 50, width = 260)
        
        
    def closePage(self):
        try:
            self.decorwidget.destroy()
            self.textwidget.destroy()
            self.burgerwidget.destroy()
            self.pancakewidget.destroy()
            self.cupcakewidget.destroy()
            self.recipe1.destroy()
            self.recipe2.destroy()
            self.recipe3.destroy()
            self.button.destroy()
        except AttributeError:
            pass
        self.showMainPage()
        
if __name__ == '__main__':
    App()