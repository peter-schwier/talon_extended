from talon import Module

mod = Module()
# this declares a tag in the user namespace (i.e. 'user.tabs')
mod.tag("fluent_search_installed", desc="Fluent Search is installed and available.")
mod.tag("fluent_search_disabled", desc="Fluent Search is currently disabled.")
