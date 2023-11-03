import npyscreen

class MenuForm(npyscreen.ActionForm):
    def create(self):
        self.add(npyscreen.TitleText, name="Opción 1:")
        self.add(npyscreen.TitleText, name="Opción 2:")
        self.add(npyscreen.TitleText, name="Opción 3:")

    def on_ok(self):
        # Realizar acciones correspondientes a las opciones
        pass

class MyTestApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", MenuForm, name="Menú de Opciones")

if __name__ == "__main__":
    app = MyTestApp()
    app.run()
