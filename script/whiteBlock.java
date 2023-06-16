import java.awt.*;
import java.awt.event.InputEvent;

public class whiteBlock {
    public static void main(String[] args) throws AWTException {
        Robot robot = new Robot();

        PointerInfo point = MouseInfo.getPointerInfo();
        robot.delay(2000);

        Point location = point.getLocation();
        int starx = (int)location.getX();
        int stary = (int)location.getY();
        System.out.println(location);
        Color color;
        int red ;
        int green ;
        int blue ;
        int step = 166;
        int release_mouse = 50;

        for(int i = 0; i < 3; i++){
            robot.mouseMove(starx, stary);
        }
        robot.delay(50);
        robot.mousePress(InputEvent.BUTTON1_MASK);
        robot.delay(50);
        robot.mouseRelease(InputEvent.BUTTON1_MASK);

        while(true){
            System.out.println("==========");
            for(int i = 0; i < 4; i++){

                color = robot.getPixelColor(starx + i*step, stary);
                red = color.getRed();
                green = color.getGreen();
                blue = color.getBlue();
                System.out.println(color);
                if(red < 200 && green < 200 && blue < 220){

                    for(int j = 0; j < 10; j++){
                        robot.mouseMove(starx + i*step, stary);
                    }


                    robot.mousePress(InputEvent.BUTTON1_MASK);
                    robot.delay(release_mouse);
                    robot.mouseRelease(InputEvent.BUTTON1_MASK);
                }
            }
            System.out.println("==========");
        }


    }
}
