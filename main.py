from controller.controller import Controller
from model.model import Model
from view.viewTkinter import ViewTkinter


controller = Controller()
model = Model("conf/conf.json")
viewTk = ViewTkinter()
controller.Model = model
controller.View = viewTk
controller.start()
