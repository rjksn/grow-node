from matplotlib.colors import LinearSegmentedColormap

colors = [(1.0000, 1.0000, 1.0000), (0.9804, 0.9804, 0.9804), (0.9647, 0.9647, 0.9647), 
          (0.9490, 0.9490, 0.9490), (0.9333, 0.9333, 0.9333), (0.9137, 0.9137, 0.9137),
          (0.8980, 0.8980, 0.8980), (0.8824, 0.8824, 0.8824), (0.8667, 0.8667, 0.8667),
          (0.8471, 0.8471, 0.8471), (0.8314, 0.8314, 0.8314), (0.8157, 0.8157, 0.8157),
          (0.8000, 0.8000, 0.8000), (0.7843, 0.7843, 0.7843), (0.7647, 0.7647, 0.7647),
          (0.7490, 0.7490, 0.7490), (0.7333, 0.7333, 0.7333), (0.7176, 0.7176, 0.7176),
          (0.6980, 0.6980, 0.6980), (0.6824, 0.6824, 0.6824), (0.6667, 0.6667, 0.6667),
          (0.6510, 0.6510, 0.6510), (0.6314, 0.6314, 0.6314), (0.6157, 0.6157, 0.6157),
          (0.6000, 0.6000, 0.6000), (0.5843, 0.5843, 0.5843), (0.5686, 0.5686, 0.5686),
          (0.5490, 0.5490, 0.5490), (0.5333, 0.5333, 0.5333), (0.5176, 0.5176, 0.5176),
          (0.5020, 0.5020, 0.5020), (0.4824, 0.4824, 0.4824), (0.4667, 0.4667, 0.4667),
          (0.4510, 0.4510, 0.4510), (0.4353, 0.4353, 0.4353), (0.4157, 0.4157, 0.4157),
          (0.4000, 0.4000, 0.4000), (0.3843, 0.3843, 0.3843), (0.3686, 0.3686, 0.3686),
          (0.3529, 0.3529, 0.3529), (0.3333, 0.3333, 0.3333), (0.3176, 0.3176, 0.3176),
          (0.3020, 0.3020, 0.3020), (0.2863, 0.2863, 0.2863), (0.2667, 0.2667, 0.2667),
          (0.2510, 0.2510, 0.2510), (0.2353, 0.2353, 0.2353), (0.2196, 0.2196, 0.2196),
          (0.2039, 0.2039, 0.2039), (0.2196, 0.2196, 0.2196), (0.2353, 0.2353, 0.2353),
          (0.2510, 0.2510, 0.2510), (0.2667, 0.2667, 0.2667), (0.2863, 0.2863, 0.2863),
          (0.3020, 0.3020, 0.3020), (0.3176, 0.3176, 0.3176), (0.3333, 0.3333, 0.3333),
          (0.3529, 0.3529, 0.3529), (0.3686, 0.3686, 0.3686), (0.3843, 0.3843, 0.3843),
          (0.4000, 0.4000, 0.4000), (0.4157, 0.4157, 0.4157), (0.4353, 0.4353, 0.4353),
          (0.4510, 0.4510, 0.4510), (0.4667, 0.4667, 0.4667), (0.4824, 0.4824, 0.4824),
          (0.5020, 0.5020, 0.5020), (0.5176, 0.5176, 0.5176), (0.5333, 0.5333, 0.5333),
          (0.5490, 0.5490, 0.5490), (0.5686, 0.5686, 0.5686), (0.5843, 0.5843, 0.5843),
          (0.6000, 0.6000, 0.6000), (0.6157, 0.6157, 0.6157), (0.6314, 0.6314, 0.6314),
          (0.6510, 0.6510, 0.6510), (0.6667, 0.6667, 0.6667), (0.6824, 0.6824, 0.6824),
          (0.6980, 0.6980, 0.6980), (0.7176, 0.7176, 0.7176), (0.7333, 0.7333, 0.7333),
          (0.7490, 0.7490, 0.7490), (0.7647, 0.7647, 0.7647), (0.7843, 0.7843, 0.7843),
          (0.8000, 0.8000, 0.8000), (0.8157, 0.8157, 0.8157), (0.8314, 0.8314, 0.8314),
          (0.8471, 0.8471, 0.8471), (0.8667, 0.8667, 0.8667), (0.8824, 0.8824, 0.8824),
          (0.8980, 0.8980, 0.8980), (0.9137, 0.9137, 0.9137), (0.9333, 0.9333, 0.9333),
          (0.9490, 0.9490, 0.9490), (0.9647, 0.9647, 0.9647), (0.9804, 0.9804, 0.9804),
          (1.0000, 1.0000, 1.0000), (0.9804, 0.9804, 0.9804), (0.9608, 0.9608, 0.9608),
          (0.9412, 0.9412, 0.9412), (0.9216, 0.9216, 0.9216), (0.9020, 0.9020, 0.9020),
          (0.8824, 0.8824, 0.8824), (0.8627, 0.8627, 0.8627), (0.8431, 0.8431, 0.8431),
          (0.8235, 0.8235, 0.8235), (0.8039, 0.8039, 0.8039), (0.7843, 0.7843, 0.7843),
          (0.7647, 0.7647, 0.7647), (0.7451, 0.7451, 0.7451), (0.7255, 0.7255, 0.7255),
          (0.7059, 0.7059, 0.7059), (0.6863, 0.6863, 0.6863), (0.6667, 0.6667, 0.6667),
          (0.6471, 0.6471, 0.6471), (0.6275, 0.6275, 0.6275), (0.6078, 0.6078, 0.6078),
          (0.5922, 0.5922, 0.5922), (0.5725, 0.5725, 0.5725), (0.5529, 0.5529, 0.5529),
          (0.5333, 0.5333, 0.5333), (0.5137, 0.5137, 0.5137), (0.4941, 0.4941, 0.4941),
          (0.4745, 0.4745, 0.4745), (0.4549, 0.4549, 0.4549), (0.4353, 0.4353, 0.4353),
          (0.4157, 0.4157, 0.4157), (0.3961, 0.3961, 0.3961), (0.3765, 0.3765, 0.3765),
          (0.3569, 0.3569, 0.3569), (0.3373, 0.3373, 0.3373), (0.3176, 0.3176, 0.3176),
          (0.2980, 0.2980, 0.2980), (0.2784, 0.2784, 0.2784), (0.2588, 0.2588, 0.2588),
          (0.2392, 0.2392, 0.2392), (0.2196, 0.2196, 0.2196), (0.2588, 0.2588, 0.3137),
          (0.3020, 0.3020, 0.4118), (0.3412, 0.3412, 0.5098), (0.3843, 0.3843, 0.6078),
          (0.4235, 0.4235, 0.7059), (0.4667, 0.4667, 0.8039), (0.5059, 0.5059, 0.9020),
          (0.5490, 0.5490, 1.0000), (0.5137, 0.5765, 0.9373), (0.4784, 0.6039, 0.8745),
          (0.4431, 0.6314, 0.8118), (0.4118, 0.6588, 0.7490), (0.3765, 0.6863, 0.6863),
          (0.3412, 0.7176, 0.6235), (0.3059, 0.7451, 0.5608), (0.2745, 0.7725, 0.4980),
          (0.2392, 0.8000, 0.4353), (0.2039, 0.8275, 0.3725), (0.1686, 0.8588, 0.3098),
          (0.1373, 0.8863, 0.2471), (0.1020, 0.9137, 0.1843), (0.0667, 0.9412, 0.1216),
          (0.0314, 0.9686, 0.0588), (0.0000, 1.0000, 0.0000), (0.0275, 1.0000, 0.0000),
          (0.0588, 1.0000, 0.0000), (0.0902, 1.0000, 0.0000), (0.1216, 1.0000, 0.0000),
          (0.1529, 1.0000, 0.0000), (0.1843, 1.0000, 0.0000), (0.2157, 1.0000, 0.0000),
          (0.2471, 1.0000, 0.0000), (0.2784, 1.0000, 0.0000), (0.3098, 1.0000, 0.0000),
          (0.3412, 1.0000, 0.0000), (0.3725, 1.0000, 0.0000), (0.4039, 1.0000, 0.0000),
          (0.4353, 1.0000, 0.0000), (0.4667, 1.0000, 0.0000), (0.4980, 1.0000, 0.0000),
          (0.5294, 1.0000, 0.0000), (0.5608, 1.0000, 0.0000), (0.5922, 1.0000, 0.0000),
          (0.6235, 1.0000, 0.0000), (0.6549, 1.0000, 0.0000), (0.6863, 1.0000, 0.0000),
          (0.7176, 1.0000, 0.0000), (0.7490, 1.0000, 0.0000), (0.7804, 1.0000, 0.0000),
          (0.8118, 1.0000, 0.0000), (0.8431, 1.0000, 0.0000), (0.8745, 1.0000, 0.0000),
          (0.9059, 1.0000, 0.0000), (0.9373, 1.0000, 0.0000), (0.9686, 1.0000, 0.0000),
          (1.0000, 1.0000, 0.0000), (1.0000, 0.9765, 0.0000), (1.0000, 0.9569, 0.0000),
          (1.0000, 0.9373, 0.0000), (1.0000, 0.9137, 0.0000), (1.0000, 0.8941, 0.0000),
          (1.0000, 0.8745, 0.0000), (1.0000, 0.8510, 0.0000), (1.0000, 0.8314, 0.0000),
          (1.0000, 0.8118, 0.0000), (1.0000, 0.7882, 0.0000), (1.0000, 0.7686, 0.0000),
          (1.0000, 0.7490, 0.0000), (1.0000, 0.7255, 0.0000), (1.0000, 0.7059, 0.0000),
          (1.0000, 0.6863, 0.0000), (1.0000, 0.6667, 0.0000), (1.0000, 0.6431, 0.0000),
          (1.0000, 0.6235, 0.0000), (1.0000, 0.6039, 0.0000), (1.0000, 0.5804, 0.0000),
          (1.0000, 0.5608, 0.0000), (1.0000, 0.5412, 0.0000), (1.0000, 0.5176, 0.0000),
          (1.0000, 0.4980, 0.0000), (1.0000, 0.4784, 0.0000), (1.0000, 0.4549, 0.0000),
          (1.0000, 0.4353, 0.0000), (1.0000, 0.4157, 0.0000), (1.0000, 0.3922, 0.0000),
          (1.0000, 0.3725, 0.0000), (1.0000, 0.3529, 0.0000), (1.0000, 0.3333, 0.0000),
          (1.0000, 0.3098, 0.0000), (1.0000, 0.2902, 0.0000), (1.0000, 0.2706, 0.0000),
          (1.0000, 0.2471, 0.0000), (1.0000, 0.2275, 0.0000), (1.0000, 0.2078, 0.0000),
          (1.0000, 0.1843, 0.0000), (1.0000, 0.1647, 0.0000), (1.0000, 0.1451, 0.0000),
          (1.0000, 0.1216, 0.0000), (1.0000, 0.1020, 0.0000), (1.0000, 0.0824, 0.0000),
          (1.0000, 0.0588, 0.0000), (1.0000, 0.0392, 0.0000), (1.0000, 0.0196, 0.0000),
          (1.0000, 0.0000, 0.0000), (1.0000, 0.0000, 0.0588), (1.0000, 0.0000, 0.1216),
          (1.0000, 0.0000, 0.1843), (1.0000, 0.0000, 0.2471), (1.0000, 0.0000, 0.3098),
          (1.0000, 0.0000, 0.3725), (1.0000, 0.0000, 0.4353), (1.0000, 0.0000, 0.4980),
          (1.0000, 0.0000, 0.5608), (1.0000, 0.0000, 0.6235), (1.0000, 0.0000, 0.6863),
          (1.0000, 0.0000, 0.7490), (1.0000, 0.0000, 0.8118), (1.0000, 0.0000, 0.8745),
          (1.0000, 0.0000, 0.9373)]

fastiecm = LinearSegmentedColormap.from_list('mylist', colors) 
