import sublime, sublime_plugin

class ToggleLightAndDark(sublime_plugin.TextCommand):
    def run(self, edit):
        prefs = sublime.load_settings("Preferences.sublime-settings")
        tasks = sublime.load_settings("PlainTasks.sublime-settings")
        light_color = "Packages/User/SublimeLinter/base16-twilight.light (SL).tmTheme"
        light_theme = "Soda Light 3.sublime-theme"
        light_tasks = "Packages/PlainTasks/tasks.hidden-tmTheme"
        dark_color = "Packages/Monokai Extended/Monokai Extended.tmTheme"
        dark_theme = "Soda Dark 3.sublime-theme"
        dark_tasks = "Packages/PlainTasks/tasks-monokai.hidden-tmTheme"

        current_color = prefs.get("color_scheme")
        new_color = dark_color if current_color == light_color else light_color
        new_theme = dark_theme if current_color == light_color else light_theme
        new_tasks = dark_tasks if current_color == light_color else light_tasks

        prefs.set("color_scheme", new_color)
        prefs.set("theme", new_theme)
        tasks.set("color_scheme", new_tasks)
