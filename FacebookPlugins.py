"""
@note: enable X
"""

from trac.core import Component
from trac.wiki.macros import WikiMacroBase


class FacebookPlugins(Component):
    """
    Support for Facebook plugins.
    """

    revision = "$Rev$"
    url = "$URL$"

    
class LikeButton(WikiMacroBase):
    """
    The [http://developers.facebook.com/docs/reference/plugins/like Like button] lets
    users share pages from your site back to their Facebook profile with one click.
    
    Examples:
    {{{
    [[LikeButton]]                                   # current page
    [[LikeButton(http://google.nl)]]                 # google.nl with default layout
    [[LikeButton(http://google.com,button)]]         # google.com with button layout
    [[LikeButton(http://google.com,box)]]            # google.com with box layout
    }}}
    """

    revision = "$Rev$"
    url = "$URL$"

    def expand_macro(self, formatter, name, args):
        """Description here.

        @param name: the actual name of the macro
        @param args: text enclosed in parenthesis at the call of the macro
        """
        options = unicode(args).split(",")
        href = self.url
        layout = 'standard' # options: 'button_count', 'box_count'
        show_faces = 'true'
        width = '450'
        height = '80'
        colorscheme = 'light' # or 'dark'
        action = 'like' # or 'recommend'
        
        if len(options) > 0:
            href = options[0]
        
        if len(options) > 1:
            layout = options[1] + "_count"

        iframe_code = '<iframe src="http://www.facebook.com/plugins/like.php?href=%s&layout=%s&show_faces=%s&width=%s&action=%s&colorscheme=%s&height=%s" scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:%spx; height:%spx;" allowTransparency="true"></iframe>' % (
                       href, layout, show_faces, width, action, colorscheme, height, width, height)
        
        return iframe_code
