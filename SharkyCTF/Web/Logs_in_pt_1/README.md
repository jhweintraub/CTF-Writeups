Prompt
```
Data printed on one of our dev application has been altered, after questioning the team responsible of its development, it doesn't seem to be their doing. The H4XX0R that changed the front seems to be a meme fan and enjoyed setting the front.

We've already closed the RCE he used, there is a sensitive database running behind it. If anyone could access it we'll be in trouble. Can you please audit this version of the application and tell us if you find anything compromising, you shouldn't be able to find the admin session.

The application is hosted at logs_in
```


Look at the Image included, on the bottom bar it shows us the filename of the controller for the PHP web page, if you click on it it takes you to the page

`http://logs_in.sharkyctf.xyz/_profiler/open?file=src/Controller/MainController.php&line=23#line23`
```
<?php
namespace App\Controller;
use Sensio\Bundle\FrameworkExtraBundle\Configuration\Route;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Bundle\FrameworkBundle\Console\Application;
use Symfony\Component\HttpKernel\KernelInterface;
use Symfony\Component\Console\Input\ArrayInput;
use Symfony\Component\Console\Output\BufferedOutput;
use App\Service\CallAPI;
use Symfony\Component\Debug\Debug;
use Symfony\Component\HttpKernel\Profiler\Profiler;
class MainController extends AbstractController
{
    /**
     * @Route("/")
     * @return Response
     */
    public function index(Profiler $profiler)
    {
        $profiler->enable();
        $request = new Request(
            $_GET,
            $_POST,
            [],
            $_COOKIE,
            $_FILES,
            $_SERVER
        );
        $method = $request->getMethod();
        return $this->render('main/main.html.twig', ['method' => $method]);
    }
    /**
     * @Route("/e48e13207341b6bffb7fb1622282247b")
     * @return Response
     */
    public function admin(KernelInterface $kernel)
    {
        $url = 'http://10.0.142.5'; // IP de l'API
        $call_api = new CallAPI();
        $request = new Request(
           $_GET,
           $_POST,
           [],
           $_COOKIE,
           $_FILES,
           $_SERVER
       );
       $method = $request->getMethod();
        $get_data = $call_api->callAPI('GET', $url.'?method='.$request->getMethod(), false);
        $response = $get_data;
        return $this->render('main/admin.html.twig', ['response' => json_decode($response), 'method' => $method]);
    }
    /**
     * @Route("/e48e13207341b6bffb7fb1622282247b/debug")
     * @return Response
     */
    public function debug(Profiler $profiler)
    {
        $profiler->enable();
        return $this->render('main/debug.html.twig');
    }
}
```

Those two misc. routes with weird nums and letters stick out to me cause they're GET routes, not POST. If you go to the e48e13207341b6bffb7fb1622282247b/debug page you get the flag


`shkCTF{0h_N0_Y0U_H4V3_4N_0P3N_SYNF0NY_D3V_M0D3_1787a60ce7970e2273f7df8d11618475}`