"""
Append Start TC to Clip Name

URL:
    https://github.com/khanrahan/append-start-tc-to-name
     
Description:
    Append the starting timecode to a clip's name.  Helps generate unique names for
    clips that are the same source, but different frame ranges.

Menus:
    Right-click selected clips on a reel  -> Edit... -> Append Start TC to Clip Name

To Install:

    For all users, copy this file to:
    /opt/Autodesk/shared/python

    For a specific user, copy this file to:
    /opt/Autodesk/user/<user name>/python
"""

from __future__ import print_function

__title__ = "Append Start TC to Clip Name"
__version_info__ = (0, 0, 1)
__version__ = ".".join([str(num) for num in __version_info__])


def tc_tidy(tc_str):
    """converts timecode from 01:01:01+01 to 01h01m01s01frm"""

    tidy = "".join([tc_str[0:2], "h", tc_str[3:5], "m", tc_str[6:8], "s", tc_str[9:11], "frm"])
    
    return tidy


def append_start_tc_to_name(selection):
    """NOTE - this will not be ctrl+z possible."""
    
    print(__title__, "v{}".format(__version__))
    print(__file__)

    for clip in selection:
        tc_start = clip.start_time.get_value().timecode
        tc_start_tidy = tc_tidy(tc_start)
        
        print("Appending", tc_start_tidy, "to", clip.name.get_value())

        clip.name = "_".join([clip.name.get_value(), tc_start_tidy])
        

def scope_timeline_sequence(selection):
    """ """

    import flame

    for item in selection:
        if isinstance(item, flame.PyClip):
            return True
        else:
            return False


def get_media_panel_custom_ui_actions():

    return [{'name': "Edit...",
             'actions': [{'name': "Append Start TC to Clip Name",
                          'isVisible': scope_timeline_sequence,
                          'execute': append_start_tc_to_name,
                          'minimumVersion': "2021"}]
           }]
