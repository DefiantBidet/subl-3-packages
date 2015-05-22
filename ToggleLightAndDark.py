import sublime, sublime_plugin

class ToggleLightAndDark(sublime_plugin.TextCommand):
    def run(self, edit):
        prefs = sublime.load_settings("Preferences.sublime-settings")
        light_color = "Packages/User/SublimeLinter/base16-twilight.light (SL).tmTheme"
        light_theme = "Soda Light 3.sublime-theme"
        dark_color = "Packages/Monokai Extended/Monokai Extended.tmTheme"
        dark_theme = "Soda Dark 3.sublime-theme"

        current_color = prefs.get("color_scheme")
        new_color = dark_color if current_color == light_color else light_color
        new_theme = dark_theme if current_color == light_color else light_theme

        prefs.set("color_scheme", new_color)
        prefs.set("theme", new_theme)
