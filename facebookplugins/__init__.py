# Copyright (c) 2010 The TracFacebookPlugins Project.
# See LICENSE.txt for details.

"""
Collection of Trac wiki macro's for U{Facebook<http://facebook.com>}'s plugins.

@see: http://developers.facebook.com/plugins
@see: http://developers.facebook.com/docs/guides/web#plugins

@note: Also support XFBML?
"""

from genshi.builder import tag

from trac.wiki.macros import WikiMacroBase
from trac.resource import get_resource_url


__all__ = ['LikeButton', 'ActivityFeed', 'Recommendations']


class FBWikiMacro(object):
    """
    Helper class for Facebook wiki macro's.
    """

    #: Base url for Facebook's plugin scripts
    fb_url = 'http://www.facebook.com/plugins'

    def abs_href(self, formatter):
        """
        Get absolute href for trac resource.

        @param formatter
        """
        return get_resource_url(self.env, formatter.resource, formatter.req.abs_href)


    def iframe(self, src, width, height):
        """
        Create iframe.
        
        @param src:     URL to display in the iframe.
        @type src:      ``str``
        @param width:   Width of the frame.
        @type width:    ``int``
        @param height:  Height of the frame.
        @type height:   ``int``
        """
        style = "border:none; overflow:hidden; width:%spx; height:%spx;" % (width, height)

        return tag.iframe(src=src, scrolling="no", frameborder="0",
                          style=style, allowTransparency="true")


class LikeButton(WikiMacroBase, FBWikiMacro):
    """
    The Like button lets users share pages from your site back to their Facebook profile with one click.

    Examples:
    {{{
    [[LikeButton]]                                   # current page
    [[LikeButton(http://google.com)]]                # google.com with default layout
    [[LikeButton(http://google.com,button)]]         # button layout
    [[LikeButton(http://google.com,box)]]            # box layout
    }}}

    Check the [http://developers.facebook.com/docs/reference/plugins/like documentation]
    for more information.
    """

    plugin_name = 'like'

    def expand_macro(self, formatter, name, args):
        """
        @param name: the actual name of the macro
        @param args: text enclosed in parenthesis at the call of the macro
        """
        options = unicode(args).split(",")
        href = self.abs_href(formatter)
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

        src = "%s/%s.php?href=%s&layout=%s&show_faces=%s&width=%s&action=%s&colorscheme=%s&height=%s" % (
              self.fb_url, self.plugin_name, href, layout, show_faces, width, action, colorscheme, height)

        return self.iframe(src, width, height)


class ActivityFeed(WikiMacroBase, FBWikiMacro):
    """
    The Activity Feed plugin displays the most interesting recent Facebook activity taking place on your site.

    Examples:
    {{{
    [[ActivityFeed]]                                 # current page
    [[ActivityFeed(http://google.com)]]              # google.com with recommendations
    [[ActivityFeed(http://google.com,false)]]        # without recommendations
    }}}

    Check the [http://developers.facebook.com/docs/reference/plugins/activity documentation]
    for more information.
    """

    plugin_name = 'activity'

    def expand_macro(self, formatter, name, args):
        """
        @param name: the actual name of the macro
        @param args: text enclosed in parenthesis at the call of the macro
        """
        options = unicode(args).split(",")
        href = self.abs_href(formatter)
        width = '300'
        height = '300'
        header = 'true'
        colorscheme = 'light' # or 'dark'
        recommendations = 'true'

        if len(options) > 0 and options[0] != "None":
            href = options[0]

        if len(options) > 1:
            recommendations = 'false'

        src = "%s/%s.php?site=%s&width=%s&height=%s&header=%s&colorscheme=%s&recommendations=%s" % (
              self.fb_url, self.plugin_name, href, width, height, header, colorscheme, recommendations)

        return self.iframe(src, width, height)


class Recommendations(ActivityFeed):
    """
    The Recommendations plugin shows personalized Facebook recommendations to your users.

    Examples:
    {{{
    [[Recommendations]]                                 # current page
    [[Recommendations(http://python.org)]]              # python.org
    }}}

    Check the [http://developers.facebook.com/docs/reference/plugins/recommendations documentation]
    for more information.
    """

    plugin_name = 'recommendations'

    def expand_macro(self, formatter, name, args):
        """
        @param name: the actual name of the macro
        @param args: text enclosed in parenthesis at the call of the macro
        """
        options = unicode(args).split(",")
        href = self.abs_href(formatter)
        width = '300'
        height = '300'
        header = 'true'
        colorscheme = 'light' # or 'dark'

        if len(options) > 0 and options[0] != "None":
            href = options[0]

        src = "%s/%s.php?site=%s&width=%s&height=%s&header=%s&colorscheme=%s" % (
              self.fb_url, self.plugin_name, href, width, height, header, colorscheme)

        return self.iframe(src, width, height)

