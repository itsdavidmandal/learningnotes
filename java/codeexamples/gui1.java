import java.awt.*; // styling haru huncha yesma 
import javax.swing.*; // 

class studentform1{
    public static void main(String[] args){
        
        //frame euta matrai huncha but the panels haru chahi dherai wata huna sakincha 
        // frame banako 
        JFrame frame = new JFrame("My frame practise ");
        frame.setVisible(true);
        frame.setSize(800,800);
        frame.setLayout(null);
        
        
        // panel banako 
        JPanel panel1 = new JPanel();
        panel1.setBounds(10,10,400,400);
        panel1.setBackground(Color.YELLOW);
        
        frame.add(panel1); // adding the panel to the frame 
        
        JButton b1 = new JButton ("Save");
        b1.setBounds(10,10,100,30);
        b1.setBackground(Color.ORANGE);
        
        panel1.add(b1);
        
        JButton b2 = new JButton ("Exit");
        b2.setBounds(10,10,100,30);
        b2.setBackground(Color.RED);
        
        panel1.add(b2);
        
        //another panel
        JPanel panel2 = new JPanel();
        panel2.setBounds(410,430,400,400);
        panel2.setBackground(Color.BLACK);
        
        frame.add(panel2); // adding the panel to the frame 
        
        JButton b3 = new JButton ("Save");
        b3.setBounds(10,430,100,30);
        b3.setBackground(Color.PINK);
        
        panel2.add(b3);
        
        JButton b4 = new JButton ("Exit");
        b4.setBounds(10,430,100,30);
        b4.setBackground(Color.GREEN);
        
        panel2.add(b4);
    }
}
