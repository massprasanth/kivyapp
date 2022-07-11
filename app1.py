from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
import cv2
import numpy as np

#import matplotlib as plt
from kivy.core.window import Window
#Window.size = (360,600)

helper = '''

<MySwiper@MDSwiperItem>

    FitImage:
        source:'utkarxh-rathore-DmBtO0VTvaY-unsplash.jpg'
        radius: [20,]


<welcomescreen> :
    BoxLayout :
        orientation : 'vertical'
        padding : 20
        Image :
            source:'blood-156063_1280.png'
            pos_hint : {'center_x' : 0.5 ,'center_y' : 0.7}
            size : self.texture_size
    
        MDLabel :
            text :" IT'S NOT JUST PAIN. ITS  A COMPLETE PHYSICAL,MENTAL AND EMOTIONAL ASSAULT IN YOUR BODY "
            pos_hint : {'center_x' : 0.5,'center_y' : 0.3}
            theme_text_color : 'Custom'
            text_color : app.theme_cls.primary_color
            radius : [20,]
    
    
    
        MDIconButton :
            icon : 'arrow-right'
            md_bg_color : app.theme_cls.primary_color
            radius : [10,0,0,0]
            icon_size:'40sp'
            pos_hint : {'center_x' : 0.95,'center_y' : 0.55}
            on_release : root.manager.current = 'welcome1'
    
<welcomescreen1> :
    BoxLayout :
        orientation : 'vertical'
        padding : 20
        Image :
            source : 'red-blood-cell-1861640_1920.png'
            pos_hint : {'center_x' : .5,'center_y' : .7}
            size : self.texture_size
        MDLabel : 
            text : 'YOU HAVE TO FIGHT THROUGH SOME BAD DAYS TO EARN THE BEST DAYS OF YOUR LIFE'
            pos_hint : {'center_x' :.52,'center_y' : .4}
            theme_text_color : 'Custom'
            text_color : app.theme_cls.primary_color
            
        MDIconButton :
            icon : 'arrow-right'
            md_bg_color : app.theme_cls.primary_color
            radius : [10,0,0,0]
            pos_hint : {'center_x' : .95,'center_y':.1}
            on_release : root.manager.current = 'menu'
            icon_size : '40sp'
<menuscreen> :
	MDBottomNavigation :
		MDBottomNavigationItem :
			name : 'menu'
			text : 'Home'
			icon : 'home'
			BoxLayout:
                orientation: 'vertical'
                padding : 10
                spacing : 10
                MDSwiper:
				    size_hint_y: None
				    height : root.height*.3
				    y: root.height - self.height - toolbar.height - dp(30)

				    MySwiper:

				    MySwiper:

				    MySwiper:

				    MySwiper:

				    MySwiper:
		    	MDLabel :
				    text : 'Hello there !!!'
				    theme_text_color : 'Custom'
				    text_color : app.theme_cls.primary_color
			    	
				    font_style : 'H6'
			    MDLabel :
			    	text : 'welcome to our application.This appication is specially designed for anemia patients. In this application the conjunctiva part of the eye is used to detect anemia'
				    pos_hint : {'center_x' : 0.5,'center_y' : 0.45}
			    MDLabel :
				    text : 'INSTRUCTIONS :'
				    pos_hint : {'center_x' : 0.5,'center_y' : 0.38}
				    theme_text_color : 'Custom'
				    text_color : app.theme_cls.primary_color
				    font_style : 'H6'
			    MDLabel :
				    text : '1. Click next button and fill patient details'
				    font_style : 'Subtitle1'
				    pos_hint : {'center_x' : 0.57,'center_y' : 0.33}
			    MDLabel :
				    text : '2. Choose your eye image with good resolution'
				    font_style : 'Subtitle1'
				    pos_hint : {'center_x' : 0.57,'center_y' : 0.29}
			    MDLabel :
				    text : '3. click result button '
				    font_style : 'Subtitle1'
				    pos_hint : {'center_x' : 0.57,'center_y' : 0.25}
		MDBottomNavigationItem :
			name : 'anemia'
			text : 'next'
			MDLabel :
				text : 'Patient Details'
				pos_hint : {'center_x' : 0.5,'center_y' : 0.85}
				font_style : 'H4'

			MDTextField :
			    id : name
				hint_text : 'Patient Name'
				required : True
				helper_text : 'Enter Patient Name'
				helper_text_mode : 'on_focus'
				pos_hint : {'center_y' : 0.8 }
				max_text_length: 20

            MDTextField :
                id : age
				hint_text : ' Age'
				helper_text : "Enter Patient's Age"
				helper_text_mode : 'on_focus'
				pos_hint : {'center_y' : 0.6}
				max_text_length: 5 

			MDTextField :
			    id : gender
				hint_text : 'Gender'
				helper_text : "Enter Patient's Gender"
				helper_text_mode : 'on_focus'
				pos_hint : {'center_y' : 0.4 }
				max_text_length: 15

			MDTextField :
			    id : blood_grp
				hint_text : 'Blood Group'
				helper_text : "Enter Patient's Blood Group"
				helper_text_mode : 'on_focus'
				pos_hint : {'center_y' : 0.2 }
				max_text_length: 20

			MDRectangleFlatButton :
				text : 'next'
				pos_hint : {'center_x' : 0.5,'center_y' : 0.1}
				on_release : root.manager.current = 'upload' if (app.root.get_screen('menu').ids.name.text and app.root.get_screen('menu').ids.age.text and app.root.get_screen('menu').ids.gender.text and app.root.get_screen('menu').ids.blood_grp.text)else app.show_dialog('Patient Details Check','enter valid  details')

	MDNavigationLayout :

		ScreenManager :

			MDScreen :
				name : 'menu'
				MDToolbar :
					id : toolbar
					title : 'Anemia'
					pos_hint : { 'top' : 1}
					left_action_items :[ ['menu',lambda x :nav_drawer.set_state('open') ]]
			MDScreen :
				name : 'anemia'
				MDLabel :
					text : 'welcome'
					halign : 'center'


		MDNavigationDrawer :
			id : nav_drawer
			type : 'modal'
			anchor : 'right'
			id : nav_drawer
			radius : (0,16,16,0) if self.anchor == 'left' else (26,0,0,26)

			MDNavigationDrawerMenu :

				MDNavigationDrawerHeader :
					title : 'Anemia'
					text : 'Non Invasive Detection'
					source : "C:/Users/DEVIGA D/Downloads/campuraai-02-removebg.png"
					spacing : '4dp'
					padding : '12dp',0,0,'56dp'	

				MDNavigationDrawerLabel :
					text : 'Contents'
				MDNavigationDrawerDivider :

				MDNavigationDrawerItem :
					icon : ''
					icon_color : app.theme_cls.primary_color
					text : 'About Anemia'
					on_release : root.manager.current = 'about'




				MDNavigationDrawerItem :
					icon : ''
					icon_color : app.theme_cls.primary_color
					text : 'Symptoms'
				    on_release : root.manager.current = 'symp'

				MDNavigationDrawerItem :
					icon : ''
					icon_color : app.theme_cls.primary_color
					text : 'Upload image'
					on_release : root.manager.current = 'upload'

				MDNavigationDrawerItem :
					icon : ''
					icon_color : app.theme_cls.primary_color
					text : 'Result page'
				MDNavigationDrawerDivider :
				MDNavigationDrawerItem :
					icon : 'coffee'
					icon_color : app.theme_cls.primary_color
					text : 'Help'
					on_release : root.manager.current = 'instruct'

				MDNavigationDrawerItem :
					icon : 'coffee'
					icon_color : app.theme_cls.primary_color
					text : 'Contact us!'
					on_release : root.manager.current = 'contact'


				MDNavigationDrawerDivider :




				MDNavigationDrawerItem :


			MDSwitch :
				pos_hint : {'center_x' : 0.9,'center_y' : 0.95}
				width : dp(35)
				on_active : app.check(*args)

<uploadScreen> :
    MDToolbar :
	    id : toolbar
		title : ''
		pos_hint : { 'top' : 1}
	BoxLayout :
	    orientation : 'vertical'
	    padding : 20
	    MDIconButton :
            icon : 'arrow-left'
            md_bg_color : app.theme_cls.primary_color
            radius : [10,0,0,0]
            pos_hint : {'center_x' : .05,'center_y' : 0.8}
            icon_size : '40sp'
            on_release : root.manager.current = 'menu' 
            
        Image : 
            source : 'red-blood-cells-4256710.jpg'
            pos_hint : {'center_x' : .5,'center_y' : .95}
            size_hint : .6,.6
            radius : [50,]
        MDRectangleFlatButton :
            text : 'Choose Image'
            pos_hint : {'center_x' :0.5,'center_y' : 0.5}
            on_release : app.open_file_manager()
    
    
        MDIconButton :
            icon : 'arrow-right'
            md_bg_color : app.theme_cls.primary_color
            radius : [10,0,0,0]
            pos_hint : {'center_x' : .95,'center_y': .05}
            icon_size : '40sp'
            on_release : root.manager.current = 'kmeans' if app.path else app.show_dialog('Input Check...','please insert your image')
    
        

<kmeansScreen> :
    MDToolbar :
	    id : toolbar
		title : ''
		pos_hint : { 'top' : 1}


	MDRectangleFlatButton :
        text : 'K-Means clusters'
        pos_hint : {'center_x' :0.5,'center_y' : 0.5}
        on_release : app.kmeans() 

    MDRectangleFlatButton :
        text : 'Result'
        pos_hint : {'center_x' :0.5,'center_y' : 0.3}
        on_release : app.result(),app.show_dialog('result','The Patient is Non-Anemic') if app.res else app.show_dialog('result','The patient is Anemic'),app.clear_details()



    MDIconButton :
        icon : 'arrow-left'
        md_bg_color : app.theme_cls.primary_color
        radius : [10,0,0,0]
        pos_hint : {'center_y' : 0.95}
        icon_size : '40sp'
        on_release : root.manager.current = 'upload'


<aboutscreen> :
    MDIconButton :
        icon : 'arrow-left'
        md_bg_color : app.theme_cls.primary_color
        radius : [10,0,0,0]
        pos_hint : { 'top' : 1}
        icon_size : '40sp'
        on_release : root.manager.current = 'menu'
    
    BoxLayout:
        orientation: 'vertical'
        padding : 10
        spacing : 20
        MDLabel :
            text : 'ABOUT :'
            pos_hint : {'center_x': 0.5,'center_y' : 0.85}
            font_style : 'H5'
            theme_text_color: "Custom"
            text_color: 0, 1, 0, 1
        MDLabel : 
            text : 'Anemia is a deficiency in the number or quality of red blood cells in your body. Red blood cells carry oxygen around your body using a particular protein called haemoglobin. Anemia means that either the level of red blood cells or the level of haemoglobin is lower than normal . The anemia can be detected non-invasively that may replace laboratory tests using a application that uses photos of conjunctiva'
            text_size: self.width, None
        MDLabel : 
            text : 'The conjunctiva is a thin membrane that lines the inside of your eyelids (both upper and lower) and covers the outer portion of the sclera. K means clustering algorithm was used to cluster an image to separate conjunctiva part. By this application, it is easy to detect whether the subject is anemic or not.'
            text_size: self.width, None
        MDLabel : 
            text : 'This application is developed by college of engineering (CEG)students(DEVIGA,BHARATHI,AYYAPPAN) under the guidance of DR.J.SAMINATHAN,teaching fellow ,department of ECE' 
            text_size: self.width, None
<symptomsscreen> :
    BoxLayout :
        orientation : 'vertical'
        padding : 20
        spacing : 20
        MDIconButton :
            icon : 'arrow-left'
            pos_hint : { 'top' : 1}
            md_bg_color : app.theme_cls.primary_color
            radius : [10,0,0,0]
            icon_size : '40sp'
            on_release : root.manager.current = 'menu'
        MDLabel :
            text : 'Symptoms'
            theme_text_color : 'Custom'
            text_color : app.theme_cls.primary_color
            pos_hint : {'center_x' : 0.5,'center_y' : 0.9}
            font_style : 'H4'
        MDLabel : 
            text : '1.Unusual tiredness'
        MDLabel : 
            text : "2.Skin that's palar than usual"
        MDLabel : 
            text : '3.Shortness of breath'
        MDLabel : 
            text : '4.Headaches'
        MDLabel : 
            text : '5.Heart palpitations'
        MDLabel : 
            text : '6.Dry and damaged hair and skin'
        MDLabel : 
            text : '7.Swelling and soreness of your tongue or mouth'
        MDLabel : 
            text : '8.Restless legs'
        MDLabel : 
            text : '9.Brittle or spoon-shaped fingernails'
        
<contactscreen> :
    
    MDIconButton :
        icon : 'arrow-left'
        pos_hint : {'center_y' : 0.95}
        md_bg_color : app.theme_cls.primary_color
        radius : [10,0,0,0]
        icon_size : '40sp'
        on_release : root.manager.current = 'menu' 
    MDLabel :
        text : 'CONTACT US:'
        pos_hint : {'center_x': 0.55,'center_y' : 0.85}
        font_style : 'H5'
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1
    MDLabel :
        text : 'anemiadetction@gmail.com'
        pos_hint : {'center_x': 0.65,'center_y' : 0.75}
        font_style : 'H5' 

<instructionsscreen> :
    MDIconButton :
        icon : 'arrow-left'
        pos_hint : {'center_y' : 0.95}
        icon_size : '40sp'
        md_bg_color : app.theme_cls.primary_color
        radius : [10,0,0,0]
        on_release : root.manager.current = 'menu' 
    MDLabel :
        text : 'INSTRUCTIONS:'
        pos_hint : {'center_x': 0.55,'center_y' : 0.85}
        font_style : 'H5'
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1
    MDLabel :
        text : 'Camera should have high resolution.'
        pos_hint : {'center_x': 0.6,'center_y' : 0.75}
        font_style : 'H5'
    MDLabel :
        text : 'Images should be taken in Ambient light condition.'
        pos_hint : {'center_x': 0.6,'center_y' : 0.65}
        font_style : 'H5'
    MDLabel :
        text : 'The optimal distance between conjunctiva and camera sholud be 8cm'
        pos_hint : {'center_x': 0.6,'center_y' : 0.55}
        font_style : 'H5'
    MDLabel :
        text : 'First, the subject is asked to lower their eyelids with their thumb to make the conjunctiva part visible.'
        pos_hint : {'center_x': 0.6,'center_y' : 0.45}
        font_style : 'H5'
    MDLabel :
        text : 'Then Image is taken and processed.'
        pos_hint : {'center_x': 0.6,'center_y' : 0.35}
        font_style : 'H5'
    MDLabel :
        text : ''
        pos_hint : {'center_x': 0.55,'center_y' : 0.75}
        font_style : 'H5'
    MDLabel :
        text : ''
        pos_hint : {'center_x': 0.55,'center_y' : 0.75}
        font_style : 'H5'
   
'''
class symptomsscreen(Screen) :
    pass

class contactscreen(Screen) :
    pass

class welcomescreen(Screen):
    pass

class welcomescreen1(Screen) :
	pass

class menuscreen(Screen):
    pass


class uploadscreen(Screen):
    pass


class kmeansscreen(Screen):
    pass


class aboutscreen(Screen):
    pass
class instructionsscreen(Screen) :
    pass


class AnemiaApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.path = None
        self.file_manager_obj = MDFileManager(
            select_path=self.select_path,
            exit_manager=self.exit_manager,
            preview=True
        )

    def select_path(self, path):
        print(path)
        self.path = path
        self.exit_manager()

    def open_file_manager(self):
        self.file_manager_obj.show('/')

    def exit_manager(self):
        self.file_manager_obj.close()

    def build(self):
        sm = ScreenManager()
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Purple'
        scr = Builder.load_string(helper)
        sm.add_widget(welcomescreen(name='welcome'))
        sm.add_widget(welcomescreen1(name='welcome1'))
        sm.add_widget(menuscreen(name='menu'))
        sm.add_widget(uploadscreen(name='upload'))
        sm.add_widget(kmeansscreen(name='kmeans'))
        sm.add_widget(aboutscreen(name='about'))
        sm.add_widget(symptomsscreen(name='symp'))
        sm.add_widget(contactscreen(name='contact'))
        sm.add_widget(instructionsscreen(name = 'instruct'))

       

        return sm

    def imshoww(self):
        if self.path:
            img = cv2.imread(self.path)
            cv2.imshow('input image', img)
            cv2.waitKey(0)
        else:
            print('please select your image ')

    def kmeans(self):
        if self.path:
            self.img = cv2.imread(self.path)
            scale_percent = 30  # percent of original size
            width = int(self.img.shape[1] * scale_percent / 100)
            height = int(self.img.shape[0] * scale_percent / 100)
            dim = (width, height)

            # resize image
            resized = cv2.resize(self.img, dim, interpolation=cv2.INTER_AREA)

            cropped_image = resized[int(resized.shape[0] / 2):resized.shape[0]]

            # cv2.imshow('cropped', cropped_image)
            # cv2.waitKey(0)

            # convert to RGB
            self.image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
            # reshape the image to a 2D array of pixels and 3 color values (RGB)
            pixel_values = self.image.reshape((-1, 3))
            # convert to float
            pixel_values = np.float32(pixel_values)
            # define stopping criteria
            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
            # number of clusters (K)
            k = 3
            _, self.labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
            # convert back to 8 bit values
            centers = np.uint8(centers)

            # flatten the labels array
            self.labels = self.labels.flatten()
            # convert all pixels to the color of the centroids
            segmented_image = centers[self.labels.flatten()]
            # reshape back to the original image dimension
            segmented_image = segmented_image.reshape(self.image.shape)
            # show the image
            # cv2.imshow('kmeans output', segmented_image)
            # cv2.waitKey(0)

            masked_image = np.copy(self.image)
            # convert to the shape of a vector of pixel values
            masked_image = masked_image.reshape((-1, 3))
            # color (i.e cluster) to disable
            cluster = 2
            clusterr = 0
            masked_image[self.labels == cluster] = [0, 0, 0]
            masked_image[self.labels == clusterr] = [0, 0, 0]

            # convert back to original shape
            masked_image = masked_image.reshape(self.image.shape)
            # show the image
            self.kmeans_img = masked_image

        else:
            print('choose image')

    def crends_check(self):
        if self.root.get_screen('menu').ids.name.text:
            return 1
        else:
            return 0

    def next(self):
        if self.path:
            pass
        else:
            print('choose image')

    def check(self, checkbox, value):
        if value:
            self.theme_cls.theme_style = 'Dark'
        else:
            self.theme_cls.theme_style = 'Light'

    def result(self):
        if self.kmeans_img.all:

            rgb_img = cv2.cvtColor(self.kmeans_img, cv2.COLOR_BGR2RGB)
            # cv2.imshow("Img",rgb_img)
            # cv2.waitKey(0)
            red_pixels = rgb_img[:, :, 2]
            green_pixels = rgb_img[:, :, 1]
            blue_pixels = rgb_img[:, :, 0]

            # Performing operations on red pixels of the extracted cropped image.
            red_pixels_ar = np.array(red_pixels)
            red_pixels_1 = np.size(np.array(red_pixels))
            red_pixels_count = np.sum(np.array(red_pixels) > 0)

            sum_red_pixels = np.sum(red_pixels_ar)

            mean_red_pixel_intensity = sum_red_pixels / red_pixels_count

            # Performing operations on green pixels of the extracted cropped image.
            green_pixels_ar = np.array(green_pixels)
            green_pixels_1 = np.size(np.array(green_pixels))
            green_pixels_count = np.sum(np.array(green_pixels) > 0)

            sum_green_pixels = np.sum(green_pixels_ar)

            mean_green_pixel_intensity = sum_green_pixels / green_pixels_count

            diff_pixels = mean_red_pixel_intensity - mean_green_pixel_intensity
            print('Red pixel intensities')
            print(mean_red_pixel_intensity)
            print('Green pixel intensities')
            print(mean_green_pixel_intensity)
            print('Difference between red and green pixel intensities')
            print(diff_pixels)

            print('Status of Patient :')
            if (diff_pixels > 46):
                self.res = 1
                print('Non-Anemic')
            else:
                self.res = 0
                print('Anemic ')
        else:
            print('something went wrong')

    def show_dialog(self, title, value):
        close_button = MDFlatButton(text='close', on_release=self.close_dialog)
        self.dialog = MDDialog(title=title, text=value, size_hint=(0.7, 1), buttons=[close_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def clear_details(self):
        self.path = ''


AnemiaApp().run()