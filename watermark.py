import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GtkLayerShell', '0.1')
from gi.repository import Gtk, Gdk, GtkLayerShell

class Watermark(Gtk.Window):
    def __init__(self):
        super().__init__(title="Watermark")

        self.set_decorated(False)
        self.set_skip_taskbar_hint(True)
        self.set_keep_above(True)
        self.set_app_paintable(True)
        self.set_accept_focus(False)
        self.set_type_hint(Gdk.WindowTypeHint.DOCK)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        box.set_margin_right(20) 
        box.set_margin_bottom(20)


        label1 = Gtk.Label(label="Активация Linux")
        label1.set_xalign(0)
        label1.get_style_context().add_class("watermark-label-large")
        box.pack_start(label1, False, False, 0)

        label2 = Gtk.Label(label="Чтобы активировать Linux, перейдите в\nраздел \"Параметры\"")
        label1.set_xalign(0)
        label2.get_style_context().add_class("watermark-label-small")
        box.pack_start(label2, False, False, 0)

        self.add(box)

        self.connect("draw", self.on_draw)

        GtkLayerShell.init_for_window(self)
        GtkLayerShell.set_layer(self, GtkLayerShell.Layer.OVERLAY)
        GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.BOTTOM, True)
        GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.RIGHT, True)
        GtkLayerShell.set_margin(self, GtkLayerShell.Edge.BOTTOM, 10)
        GtkLayerShell.set_margin(self, GtkLayerShell.Edge.RIGHT, 10)

        self.show_all()

    def on_draw(self, widget, cr):
        cr.set_source_rgba(0, 0, 0, 0)
        cr.set_operator(cr.OPERATOR_SOURCE)
        cr.paint()
        cr.set_operator(cr.OPERATOR_OVER)
        return False

css = b"""
.watermark-label-large {
    font-size: 16px;
    color: rgba(255, 255, 255, 0.5);
}
.watermark-label-small {
    font-size: 12px;
    color: rgba(255, 255, 255, 0.3);
}
"""

style_provider = Gtk.CssProvider()
style_provider.load_from_data(css)
Gtk.StyleContext.add_provider_for_screen(
    Gdk.Screen.get_default(), style_provider,
    Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)

win = Watermark()
Gtk.main()
