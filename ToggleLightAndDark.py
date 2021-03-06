import sublime, sublime_plugin

class ToggleLightAndDark(sublime_plugin.TextCommand):
    def run(self, edit):
        prefs = sublime.load_settings("Preferences.sublime-settings")
        tasks = sublime.load_settings("PlainTasks.sublime-settings")
        light_color = "Packages/User/SublimeLinter/base16-twilight.light (SL).tmTheme"
        light_theme = "Soda Light 3.sublime-theme"
        light_tasks = "Packages/PlainTasks/tasks.hidden-tmTheme"
        dark_color = "Packages/Theme - Monokai Pro/Monokai Pro (Filter Octagon).tmTheme"
        dark_theme = "Monokai Pro (Filter Octagon).sublime-theme"
        dark_tasks = "Packages/User/tasks-monokai-pro-octagon.hidden-tmTheme"

        current_color = prefs.get("color_scheme")
        new_color = dark_color if current_color == light_color else light_color
        new_theme = dark_theme if current_color == light_color else light_theme
        new_tasks = dark_tasks if current_color == light_color else light_tasks

        prefs.set("color_scheme", new_color)
        prefs.set("theme", new_theme)
        tasks.set("color_scheme", new_tasks)
