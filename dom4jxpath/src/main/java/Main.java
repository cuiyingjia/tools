
import java.util.List;
import org.dom4j.Document;
import org.dom4j.Node;
import org.dom4j.io.SAXReader;
public class Main {

    public static void main(String[] args) throws Exception{

        SAXReader saxReader=new SAXReader();
        Document document=saxReader.read("src/main/resources/test.xml");
        List<Node>list=document.selectNodes("//name");
        for(int i=0;i<list.size();i++)
            System.out.println(list.get(i).getText());

    }

}
