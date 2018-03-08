"""
This module uses ROSEGRAPHICS to demonstrate:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES.

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Zhengxiao Zou.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

########################################################################
#
# TODO: 2.
#   RUN this program.  Then answer the following,
#     GETTING HELP AS NEED! (Ask questions!!!)
#
#     a. For the RoseGraphics coordinate system:
#
#        -- Where is the (0, 0) point on the screen?
#              Top left corner.
#
#        -- In what direction on the screen does the positive X-axis point?
#              To the right.
#
#        -- In what direction on the screen does the positive Y-axis point?
#              Downward.
#
#     b. Write a line of code that constructs a basic RoseWindow object:
#            window = rg.RoseWindow()
#
#     c. What is the default height of a RoseWindow?
#          Type into  main  the code shown in your answer above.  That will
#          ask PyCharm will help you figure out the answer to this question.
#          Hint: After you type the   (   in the line of code,
#          if you wait a moment PyCharm will add the   )   and has a popup.
#            300
#
#     d. Write a line of code that constructs a RoseWindow object whose
#        height is 100 with any width you choose.
#           Again try to use PyCharm's hints to help you figure this out.
#               window = rg.RoseWindow(100,100)
#
#     e. Use the DOT trick to answer the following:
#
#          -- Write the names of two types of graphics objects
#             that you can construct OTHER than Circle and Point:
#                polygon,ellipse
#
#          -- Write the names of three METHODs that Circle objects have:
#               Hint: Use the circle from the  example3  function below with
#               the dot trick to let PyCharm help you.
#                  attach_to , clone, detach_from
#
#          -- Write the names of three INSTANCE VARIABLEs
#             that Circle objects have:
#                center_point, radius, circle
#
#     f. What does a RoseWindow RENDER method do?
#            render draw the objects
#
#     g. When is a RoseWindow close_on_mouse_click method call necessary?  Why?
#            The close_on_mouse_click method is necessary after finish drawing everything to the screen.
#           The window will keep opening without this method.
#
#   ASK QUESTIONS ** NOW ** if you do not understand how the
#     RoseGraphics graphics system works.
#
#   When you are confident that you have written correct answers
#   to the above questions (ASK QUESTIONS AS NEEDED!),
#   change the above TO DO to DONE.
#
########################################################################

import rosegraphics as rg


def main():
    """
    Uses ROSEGRAPHICS to demonstrate:
      -- CONSTRUCTING objects,
      -- applying METHODS to them, and
      -- accessing their DATA via INSTANCE VARIABLES
    """
    example1()
    example2()
    example3()



def example1():
    """ Displays an empty window. """
    window = rg.RoseWindow(500, 300, 'Example 1: An empty window')
    window.close_on_mouse_click()


def example2():
    """ Displays two Point objects. """
    # -------------------------------------------------------------------------
    # Construct the window in which objects will be drawn.
    # -------------------------------------------------------------------------
    window = rg.RoseWindow()

    # -------------------------------------------------------------------------
    # Construct some rg.Point objects.
    # Note: the y-axis goes DOWN from the TOP.
    # -------------------------------------------------------------------------
    point1 = rg.Point(100, 150)
    point2 = rg.Point(200, 50)

    # -------------------------------------------------------------------------
    # A RoseGraphics object is not associated with a window,
    # and hence are not drawn, until you ATTACH it to a window.
    # -------------------------------------------------------------------------
    point1.attach_to(window)
    point2.attach_to(window)

    # -------------------------------------------------------------------------
    # And they still are not DRAWN until you RENDER the window.
    # That will draw ALL the objects on the window.
    # This two-step approach is important for animation.
    # -------------------------------------------------------------------------
    window.render()

    window.close_on_mouse_click()


def example3():
    """ Displays a Circle and a Rectangle. """
    # -------------------------------------------------------------------------
    # RoseWindow: optionally takes its width and height.
    # -------------------------------------------------------------------------
    width = 700
    height = 400
    window = rg.RoseWindow(width, height)

    # -------------------------------------------------------------------------
    # Circle: needs its center and radius.
    # Has  fill_color  instance variable.
    # -------------------------------------------------------------------------
    center_point = rg.Point(300, 100)
    radius = 50
    circle = rg.Circle(center_point, radius)
    circle.fill_color = 'green'
    circle.attach_to(window)


    # -------------------------------------------------------------------------
    # Rectangle: needs two opposite corners.
    # -------------------------------------------------------------------------
    point1 = rg.Point(100, 150)
    point2 = rg.Point(200, 50)
    rectangle = rg.Rectangle(point1, point2)
    rectangle.attach_to(window)

    # -------------------------------------------------------------------------
    # render: Draw ALL the objects attached to this window.
    # -------------------------------------------------------------------------
    window.render()

    # -------------------------------------------------------------------------
    # A Rectangle has instance variables  corner_1  and  corner2.
    # -------------------------------------------------------------------------
    corner1 = rectangle.corner_1
    corner2 = rectangle.corner_2
    print(corner1, corner2)  # You can also PRINT RoseGraphics objects.
    print(rectangle)  # See the Console for the output.

    # -------------------------------------------------------------------------
    # close_on_mouse_click: Keeps the window open until user clicks.
    # -------------------------------------------------------------------------
    window.close_on_mouse_click()


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
