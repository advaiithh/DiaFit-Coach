import webbrowser
import tkinter as tk
from tkinter import ttk, messagebox
import time

EXERCISE_DB = {
    'low': {
        'young': {
            'indoor': {
                'Yoga': {
                    'duration': '20 mins',
                    'instructions': [
                        "Start in mountain pose",
                        "Gentle spinal twists",
                        "Downward dog (30 sec)",
                        "Child's pose finish"
                    ],
                    'video': 'https://youtu.be/zLhyXg0hlUI?si=03T75AIOr0DjKw4Q'
                },
                'Resistance Band Training': {
                    'duration': '25 mins',
                    'instructions': [
                        "Secure band under feet",
                        "Bicep curls (3x12)",
                        "Lateral raises",
                        "Chest opener stretches"
                    ],
                    'video': 'https://youtu.be/cQWk9X2d3x8?si=pBG-iewJgY2Uy7y1M'
                },
                'Bodyweight Circuit': {
                    'duration': '30 mins',
                    'instructions': [
                        "3 rounds: 10 squats",
                        "8 knee push-ups",
                        "12 lunges",
                        "30s plank"
                    ],
                    'video': 'https://youtu.be/JCHCH7ig864?si=9L5NocLQajScd9wV'
                }
            },
            'outdoor': {
                'Brisk Walking': {
                    'duration': '30 mins',
                    'instructions': [
                        "3-4 mph pace",
                        "Swing arms naturally",
                        "Proper footwear",
                        "Stay hydrated"
                    ],
                    'video': 'https://youtu.be/FILCMapAYqM?si=BRe7ir3Y3v6i0bVc'
                },
                'Cycling': {
                    'duration': '40 mins',
                    'instructions': [
                        "Adjust seat height",
                        "Steady cadence",
                        "Low resistance",
                        "5min cool down"
                    ],
                },
                'Swimming': {
                    'duration': '25 mins',
                    'instructions': [
                        "Warm-up laps",
                        "Alternate strokes",
                        "Kickboard drills",
                        "Cool down"
                    ],
                }
            }
        },
        'medium': {
            'indoor': {
                'Chair Yoga': {
                    'duration': '15 mins',
                    'instructions': [
                        "Seated cat-cow",
                        "Overhead stretches",
                        "Forward bend",
                        "Spinal twists"
                    ],
                    'video': 'https://youtu.be/ihcBeW0eMWc?si=Kxe0QOhcNlakjcPS'
                },
                'Light Weights': {
                    'duration': '20 mins',
                    'instructions': [
                        "Bicep curls (2kg)",
                        "Overhead press",
                        "Lateral raises",
                        "Tricep extensions"
                    ],
                    'video': 'https://youtu.be/ePylP2XmNRs?si=Cpblz91ElwCQX33v'
                },
                'Indoor Cycling': {
                    'duration': '25 mins',
                    'instructions': [
                        "5min warm-up",
                        "Interval training",
                        "60-70 RPM",
                        "Cool down"
                    ],
                }
            },
            'outdoor': {
                'Nature Walk': {
                    'duration': '35 mins',
                    'instructions': [
                        "Scenic route",
                        "Steady pace",
                        "Deep breathing",
                        "Stretch breaks"
                    ],
                },
                'Golf': {
                    'duration': '9 holes',
                    'instructions': [
                        "Push cart use",
                        "Smooth swings",
                        "Walk between holes",
                        "Hydrate"
                    ],
                },
                'Tai Chi': {
                    'duration': '20 mins',
                    'instructions': [
                        "Follow instructor",
                        "Balance focus",
                        "Slow movements",
                        "Deep breathing"
                    ],
                    'video': 'https://youtu.be/ASlJ_ci_G5Y?si=dqvM-vJVLDxp5MWv'
                }
            }
        },
        'older': {
            'indoor': {
                'Seated Leg Lifts': {
                    'duration': '10 mins',
                    'instructions': [
                        "Upright posture",
                        "Alternate legs",
                        "5sec holds",
                        "10 reps/side"
                    ],
                    'video': 'https://youtu.be/fAhHS10FDPU?si=BWuUbEeXdLVbgqg6'
                },
                'Arm Circles': {
                    'duration': '8 mins',
                    'instructions': [
                        "Stand shoulder-width",
                        "Forward circles",
                        "Reverse direction",
                        "1min/side"
                    ],
                    'video': 'https://youtu.be/UVMEnIaY8aU?si=ewWX2vJzVACn-NKC'
                },
                'Breathing Exercises': {
                    'duration': '10 mins',
                    'instructions': [
                        "4-2-6 breathing",
                        "Diaphragmatic focus",
                        "Comfortable seat",
                        "Relaxation"
                    ],
                    'video': 'https://youtu.be/ORJ75RUmCk8?si=evC6u9thjh7xpLTPQ'
                }
            },
            'outdoor': {
                'Park Walk': {
                    'duration': '20 mins',
                    'instructions': [
                        "2-3 mph pace",
                        "Use walking aid",
                        "Bench rests",
                        "Enjoy nature"
                    ],
                },
                'Gardening': {
                    'duration': '30 mins',
                    'instructions': [
                        "Ergonomic tools",
                        "Alternate tasks",
                        "Knee protection",
                        "Frequent breaks"
                    ],
                },
                'Stretching': {
                    'duration': '15 mins',
                    'instructions': [
                        "Neck rotations",
                        "Shoulder rolls",
                        "Calf stretches",
                        "Seated forward bend"
                    ],
                    'video': 'https://youtu.be/sTANio_2E0Q'
                }
            }
        }
    },
    'normal': {
        'young': {
            'indoor': {
                'HIIT Workout': {
                    'duration': '20 mins',
                    'instructions': [
                        "Dynamic warm-up",
                        "30s sprints",
                        "1min recovery",
                        "8 cycles"
                    ],
                    'video': 'https://youtu.be/OpSyWP7OL6s?si=LDdY55sCuGbBzasv'
                },
                'Weight Training': {
                    'duration': '30 mins',
                    'instructions': [
                        "Barbell squats",
                        "Bench press",
                        "Deadlifts",
                        "Cool down"
                    ],
                    'video': 'https://youtu.be/dix6n1ZfSKY?si=5zLjVmcxOtVYNXoq'
                },
                'Dance Aerobics': {
                    'duration': '25 mins',
                    'instructions': [
                        "Follow routine",
                        "Low-impact moves",
                        "Moderate intensity",
                        "Hydrate"
                    ],
                    'video': 'https://youtu.be/7TLk7pscICk'
                }
            },
            'outdoor': {
                'Jogging': {
                    'duration': '30 mins',
                    'instructions': [
                        "5min warm-up",
                        "5mph pace",
                        "Even terrain",
                        "Cool down"
                    ],
                    'video': 'https://youtu.be/eSWG7XBrBBo?si=eJLJGv371HONTKjY'
                },
                'Cycling': {
                    'duration': '45 mins',
                    'instructions': [
                        "Hill intervals",
                        "60-80 RPM",
                        "Heart rate monitor",
                        "Hydrate"
                    ],
                    'video': 'https://youtu.be/oA6GaMyU_uU?si=e-_5laZBHRznbNpO'
                },
                'Sports Drills': {
                    'duration': '40 mins',
                    'instructions': [
                        "Agility ladder",
                        "Cone sprints",
                        "Plyometrics",
                        "Stretching"
                    ],
                    'video': 'https://youtu.be/7TLk7pscICk'
                }
            }
        },
        'medium': {
            'indoor': {
                'Treadmill': {
                    'duration': '30 mins',
                    'instructions': [
                        "Incline intervals",
                        "Speed variations",
                        "3-5% incline",
                        "Cool down"
                    ],
                    'video': 'https://youtube.com/shorts/W7JQizdRjDc?si=RlFdxLBs_lXns9cK'
                },
                'Circuit Training': {
                    'duration': '35 mins',
                    'instructions': [
                        "5 stations",
                        "Bodyweight exercises",
                        "30s rests",
                        "3 rounds"
                    ],
                    'video': 'https://youtu.be/7TLk7pscICk'
                },
                'Yoga': {
                    'duration': '25 mins',
                    'instructions': [
                        "Vinyasa flow",
                        "30s holds",
                        "Breath focus",
                        "Savasana"
                    ],
                    'video': 'https://youtu.be/VaoV1PrYft4'
                }
            },
            'outdoor': {
                'Hiking': {
                    'duration': '60 mins',
                    'instructions': [
                        "Moderate trail",
                        "Trekking poles",
                        "3mph pace",
                        "Breaks"
                    ],
                    'video': 'https://youtu.be/bdNlv0MimJI?si=sL2FRbNKoXVbntDX'
                },
                'Tennis': {
                    'duration': '45 mins',
                    'instructions': [
                        "Footwork focus",
                        "Serve practice",
                        "Moderate rallies",
                        "Hydrate"
                    ],
                    'video': 'https://youtube.com/shorts/dIptTnc5pMU?si=bKHJ2U3gwT2Kb1Bo'
                },
                'Swimming': {
                    'duration': '30 mins',
                    'instructions': [
                        "Freestyle laps",
                        "Backstroke alternates",
                        "Pull buoy use",
                        "Cool down"
                    ],
                    'video': 'https://youtu.be/pFN2n7CRqhw'
                }
            }
        },
        'older': {
            'indoor': {
                'Water Aerobics': {
                    'duration': '30 mins',
                    'instructions': [
                        "Aqua jogging",
                        "Leg lifts",
                        "Arm circles",
                        "Noodle use"
                    ],
                    'video': 'https://youtu.be/pFN2n7CRqhw'
                },
                'Resistance Bands': {
                    'duration': '20 mins',
                    'instructions': [
                        "Seated rows",
                        "Bicep curls",
                        "Lateral raises",
                        "2x12 reps"
                    ],
                    'video': 'https://youtube.com/shorts/9I4qtfZzw-U?si=gtZy9S5pqQ_RVvcn'
                },
                'Chair Yoga': {
                    'duration': '25 mins',
                    'instructions': [
                        "Sun salutations",
                        "Neck stretches",
                        "Spinal twists",
                        "Relaxation"
                    ],
                    'video': 'https://youtu.be/4ZpkRAcgws4'
                }
            },
            'outdoor': {
                'Walking Club': {
                    'duration': '40 mins',
                    'instructions': [
                        "Group pace",
                        "Flat paths",
                        "Social interaction",
                        "Stretching"
                    ],
                    'video': 'https://youtu.be/yQeeOQb1Yq4?si=sSojKzOgPgG2X43k'
                },
                'Tai Chi': {
                    'duration': '30 mins',
                    'instructions': [
                        "Follow instructor",
                        "Slow movements",
                        "Balance focus",
                        "Mindful breathing"
                    ],
                    'video': 'https://youtu.be/-CJf7bVR2qs?si=JarkP1uKfK8eLT1O'
                },
                'Gardening': {
                    'duration': '45 mins',
                    'instructions': [
                        "Knee pad use",
                        "Task rotation",
                        "Proper lifting",
                        "Frequent breaks"
                    ],
                    'video': 'https://youtube.com/shorts/HdzskAEH7lk?si=J5GP6PUs74RHzTiu'
                }
            }
        }
    },
'high': {
        'young': {
            'indoor': {
                'Chair Aerobics': {
                    'duration':'25 mins',
                    'instructions': [
                        "Seated marching",
                        "Arm pumps",
                        "Leg extensions",
                        "Torso twists"
                    ],

                    'video': 'https://youtu.be/u_O0pZspYec?feature=shared'
                },
                'Gentle Cycling': {
                    'duration': '30 mins',
                    'instructions': [
                        "Low resistance",
                        "Upright position",
                        "Paved paths",
                        "Frequent rests"
                    ],
                    'video': 'https://youtu.be/0MLnC3bzXgQ?feature=shared'
                },
                'Outdoor Yoga': {
                    'duration': '20 mins',
                    'instructions': [
                        "Sun salutations",
                        "Modified tree pose",
                        "Seated twists",
                        "Guided meditation"
                    ],
                    'video': 'https://youtu.be/VaoV1PrYft4'
                }
            }
        },
        'medium': {
            'indoor': {
                'Seated Exercises': {
                    'duration': '20 mins',
                    'instructions': [
                        "Supported leg lifts",
                        "Arm circles",
                        "Ankle pumps",
                        "Neck stretches"
                    ],
                    'video': 'https://youtu.be/BSnYWGqtPy8?feature=shared'
                },
                'Resistance Bands': {
                    'duration': '15 mins',
                    'instructions': [
                        "Chest presses",
                        "Seated rows",
                        "Lateral pulls",
                        "1x10 reps"
                    ],
                    'video': 'https://youtu.be/Bw1-oIu6Oi4?feature=shared'
                },
                'Balance Training': {
                    'duration': '10 mins',
                    'instructions': [
                        "Chair-assisted stands",
                        "Heel-toe walking",
                        "Single-leg stance",
                        "Weight shifts"
                    ],
                    'video': 'https://youtu.be/uth_9K3EmDI?feature=shared'
                }
            },
            'outdoor': {
                'Park Walks': {
                    'duration': '20 mins',
                    'instructions': [
                        "Benches available",
                        "Flat paths",
                        "Assistive devices",
                        "2mph pace"
                    ],
                },
                'Gardening': {
                    'duration': '30 mins',
                    'instructions': [
                        "Raised beds",
                        "Sitting breaks",
                        "Light digging",
                        "Hydration"
                    ],
                },
                'Stretching': {
                    'duration': '15 mins',
                    'instructions': [
                        "Calf stretches",
                        "Shoulder opener",
                        "Seated hamstring",
                        "Deep breathing"
                    ],
                    'video': 'https://youtu.be/sTANio_2E0Q'
                }
            }
        },
        'older': {
            'indoor': {
                'Arm Exercises': {
                    'duration': '10 mins',
                    'instructions': [
                        "Shoulder rolls",
                        "Wrist circles",
                        "No-weight curls",
                        "Light overhead press"
                    ],
                    'video': 'https://youtu.be/IC8SfzaG8_A?feature=shared'
                },
                'Leg Lifts': {
                    'duration': '8 mins',
                    'instructions': [
                        "Seated extensions",
                        "Ankle pumps",
                        "Knee marches",
                        "2x5 reps"
                    ],
                    'video': 'https://youtu.be/NbYTSPqq1R4?feature=shared'
                },
                'Breathing Drills': {
                    'duration': '10 mins',
                    'instructions': [
                        "Pursed-lip breathing",
                        "Diaphragmatic focus",
                        "4-7-8 technique",
                        "Guided relaxation"
                    ],
                    'video': 'https://youtu.be/sTANio_2E0Q'
                }
            },
            'outdoor': {
                'Supervised Walk': {
                    'duration': '15 mins',
                    'instructions': [
                        "Caregiver陪同",
                        "Flat surface",
                        "Assistive device",
                        "Frequent rests"
                    ],
                    'video': 'https://youtu.be/1_78DMfC1cw?feature=shared'
                },
                'Porch Exercises': {
                    'duration': '10 mins',
                    'instructions': [
                        "Seated marching",
                        "Arm circles",
                        "Neck stretches",
                        "Ankle rotations"
                    ],
                    'video': 'https://youtu.be/mHuO3pbOrk4?feature=shared'
                },
                'Sunlight Exposure': {
                    'duration': '20 mins',
                    'instructions': [
                        "Morning light",
                        "Gentle stretching",
                        "Vitamin D synthesis",
                        "Hydration"
                    ],
                }
            }
        }
    }
}


