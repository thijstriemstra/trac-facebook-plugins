# Copyright (c) 2010 The TracFacebookPlugins Project.
# See LICENSE.txt for details.

"""
Collection of Trac wiki macro's for U{Facebook<http://facebook.com>}'s plugins.

@see: http://developers.facebook.com/plugins
@see: http://developers.facebook.com/docs/guides/web#plugins

@note: Also support XFBML?
"""

from trac.wiki.macros import WikiMacroBase
from trac.resource import get_resource_url


class FBWikiMacro(object):

    fb_url = 'http://www.facebook.com/plugins'

    def _abs_href(self, formatter):
        """
        Get absolute href for trac resource.

        @param formatter
        """
        return get_resource_url(self.env, formatter.resource, formatter.req.abs_href)


class LikeButton(WikiMacroBase, FBWikiMacro):
    """
    The [http://developers.facebook.com/docs/reference/plugins/like Like button] lets
    users share pages from your site back to their [http://facebook.com Facebook]
    profile with one click.

    Examples:
    {{{
    [[LikeButton]]                                   # current page
    [[LikeButton(http://google.com)]]                # google.com with default layout
    [[LikeButton(http://google.com,button)]]         # button layout
    [[LikeButton(http://google.com,box)]]            # box layout
    }}}
    """

    plugin_name = 'like'

    def expand_macro(self, formatter, name, args):
        """
        @param name: the actual name of the macro
        @param args: text enclosed in parenthesis at the call of the macro
        """
        options = unicode(args).split(",")
        href = self._abs_href(formatter)
        layout = 'standard' # options: 'button_count', 'box_count'
        show_faces = 'true'
        width = '450'
        height = '80'
        colorscheme = 'light' # or 'dark'
        action = 'like' # or 'recommend'

        if len(options) > 0 and options[0] != "None":
            href = options[0]

        if len(options) > 1:
            layout = options[1] + "_count"

        iframe_code = '<iframe src="%s/%s.php?href=%s&layout=%s&show_faces=%s&width=%s&action=%s&colorscheme=%s&height=%s" scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:%spx; height:%spx;" allowTransparency="true"></iframe>' % (
                       self.fb_url, self.plugin_name, href, layout, show_faces, width, action, colorscheme, height, width, height)

        return iframe_code


class ActivityFeed(WikiMacroBase, FBWikiMacro):
    """
    The [http://developers.facebook.com/docs/reference/plugins/activity Activity Feed]
    plugins displays the most interesting recent [http://facebook.com Facebook] activity
    taking place on your site.

    Examples:
    {{{
    [[ActivityFeed]]                                 # current page
    [[ActivityFeed(http://google.com)]]              # google.com with recommendations
    [[ActivityFeed(http://google.com,false)]]        # without recommendations
    }}}
    """

    plugin_name = 'activity'

    def expand_macro(self, formatter, name, args):
        """
        @param name: the actual name of the macro
        @param args: text enclosed in parenthesis at the call of the macro
        """
        options = unicode(args).split(",")
        href = self._abs_href(formatter)
        width = '300'
        height = '300'
        header = 'true'
        colorscheme = 'light' # or 'dark'
        recommendations = 'true'

        if len(options) > 0 and options[0] != "None":
            href = options[0]

        if len(options) > 1:
            recommendations = 'false'

        iframe_code = '<iframe src="%s/%s.php?site=%s&width=%s&height=%s&header=%s&colorscheme=%s&recommendations=%s" scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:%spx; height:%spx;" allowTransparency="true"></iframe>' % (
                       self.fb_url, self.plugin_name, href, width, height, header, colorscheme, recommendations, width, height)

        return iframe_code
