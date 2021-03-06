#!/usr/bin/python3
'''
App prints pressed button
source: http://urwid.org/tutorial/index.html#global-input
'''
import urwid

def show_or_exit(key):
  if key in ('q', 'Q'):
    raise urwid.ExitMainLoop()
  txt.set_text(repr(key))

txt = urwid.Text(u"Press any key or 'Q' for quit.")
fill = urwid.Filler(txt, 'top')
loop = urwid.MainLoop(fill, unhandled_input=show_or_exit)
loop.run()

