import random

class SpiderDNA:
    def __init__(self):
        # GENETIC PARAMETERS - encoded in DNA
        self.MAX_BRIDGE_ATTEMPTS = 5
        self.FRAME_THREADS = random.randint(2, 5)
        self.RADIAL_LINES = random.randint(12, 30)
        self.TEMP_SPIRAL_ROUNDS = random.randint(3, 6)
        self.STICKY_SPIRAL_ROUNDS = random.randint(8, 15)
        self.MAX_FAILED_ANCHORS = 3
        
        # State of illegal construction 
        self.threads_built = []
        self.failed_anchors = 0
  
    # Spider senses physical tension through leg mechanoreceptors  
    def sense_tension(self, thread_type, attempt_number):
	
        # DNA-encoded tension thresholds for different thread types
        tension_thresholds = {
            'bridge': 4, 'frame': 3, 'radial': 2, 'spiral': 1
        }
        
        # Fewer attempts = higher chance (fresh silk, better position)
        threshold = tension_thresholds.get(thread_type, 2)
        return attempt_number <= threshold

	# Release silk thread
    def release_silk(self):
	    print("Fly!")
        return True
    
    # Anchor thread if tension is adequate
    def anchor_thread(self, thread_type, attempt):
        if self.sense_tension(thread_type, attempt):
            thread_name = f"{thread_type}_{len(self.threads_built)+1}"
            self.threads_built.append(thread_name)
            print(f"✓ Anchored: {thread_name}")
            self.failed_anchors = 0
            return True
        else:
            self.failed_anchors += 1
            print(f"✗ No tension - thread {attempt} failed")
            return False
 
    # 🧬INSTINCT 1: Create initial bridge between anchor points
    def build_bridge_thread(self):
        for attempt in range(1, self.MAX_BRIDGE_ATTEMPTS + 1):
            self.release_silk()
            print(f"Attempt {attempt}: Releasing bridge thread...")
            if self.anchor_thread('bridge', attempt):
                self.position = "bridge_center"
                return True               
            if self.failed_anchors >= self.MAX_FAILED_ANCHORS:
                print("✗ Location unsuitable - abandoning web site")
                return False
                
        print("✗ Bridge construction failed - seeking new location")
        return False
    
    # 🧬INSTINCT 2: Create supporting frame
    def build_frame_structure(self):
        for i in range(self.FRAME_THREADS):
            self.release_silk()
            print(f"Go web {i+1}:")
            self.anchor_thread('frame', 1)   
        self.position = "frame_complete"
    
    # 🧬INSTINCT 3: Create radial lines from center
    def build_radial_spokes(self):
        for i in range(self.RADIAL_LINES):
            self.release_silk()
            self.anchor_thread('radial', 1)
        self.position = "radials_complete"
    
    # 🧬INSTINCT 4: Create temporary spacing spiral
    def build_temporary_scaffold(self):    
        for round in range(1, self.TEMP_SPIRAL_ROUNDS + 1):
            self.release_silk()
            self.anchor_thread('temp_spiral', 1)
    
    # 🧬INSTINCT 5: Build sticky capture spiral (inward)   
    def build_capture_spiral(self):
        # Work inward, removing temporary spiral as we go
        for round in range(1, self.STICKY_SPIRAL_ROUNDS + 1):
            self.release_silk()
            # Add sticky droplets to silk for prey capture
            self.anchor_thread('sticky_spiral', 1)

	# Execute genetic_program.exe  
    def express_web_building_genes(self):
        print("SPIDER DNA ACTIVATION!!!")
		print("Booting SpiderOS🕷️")
        print("Loading web_builder.dll...")
        print("Initializing eight-legged multitasking...")
        if self.build_bridge_thread():
		    print("Phase 1: Making orders at Spider IKEA")
            self.build_frame_structure()
			print("Phase 2: Geometry class paying off")
            self.build_radial_spokes() 
			print("Phase 3: OSHA safety compliance")
            self.build_temporary_scaffold()
			print("Phase 4: Serving the table")
            self.build_capture_spiral()
        else:
		    fail_messages = [
                "This web site is not available",
                "I just realized that I'm afraid of heights.",
                "Construction budget exceeded!",
                "У цього місця погана енергетика.",
                "My GPS says... 'recalculating route'...",
				]
            print(random.choice(fail_messages))

if __name__ == "__main__":
    spider = SpiderDNA()
    spider.express_web_building_genes()
