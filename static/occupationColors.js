const occupationColors = {
  POLITICIAN: '#3498db', // Blue
  ACTOR: '#e74c3c', // Red
  WRITER: '#9b59b6', // Purple
  SINGER: '#1abc9c', // Turquoise
  ATHLETE: '#f1c40f', // Yellow
  MUSICIAN: '#2ecc71', // Green
  RELIGIOUS_FIGURE: '#d35400', // Orange
  FILM_DIRECTOR: '#7f8c8d', // Gray
  MILITARY_PERSONNEL: '#34495e', // Navy Blue
  PAINTER: '#16a085', // Dark Turquoise
  COMPOSER: '#8e44ad', // Dark Purple
  PHILOSOPHER: '#27ae60', // Dark Green
  NOBLEMAN: '#2980b9', // Light Blue
  BIOLOGIST: '#f39c12', // Dark Yellow
  MATHEMATICIAN: '#c0392b', // Dark Red
  PHYSICIST: '#e67e22', // Pumpkin
  COMPANION: '#95a5a6', // Light Gray
  BUSINESSPERSON: '#bdc3c7', // Silver
  SOCIAL_ACTIVIST: '#6C3483', // Plum
  ASTRONOMER: '#138D75', // Sea Green
  ASTRONAUT: '#D68910', // Dark Orange
  CHEMIST: '#2471A3', // Cobalt Blue
  PHYSICIAN: '#A04000', // Brown
  ARCHITECT: '#717D7E', // Metal Gray
  EXPLORER: '#283747', // Dark Slate Gray
  INVENTOR: '#1B4F72', // Dark Blue
  HISTORIAN: '#CB4335', // Brick Red
  ENGINEER: '#CA6F1E', // Bronze
  ECONOMIST: '#A9CCE3', // Light Blue Gray
  EXTREMIST: '#D5DBDB', // Off White
  COMPUTER_SCIENTIST: '#D98880', // Pastel Red
  SCULPTOR: '#D0ECE7', // Pale Turquoise
  PSYCHOLOGIST: '#AED6F1', // Light Cornflower Blue
  COMIC_ARTIST: '#A3E4D7', // Light Sea Green
  LINGUIST: '#F9E79F', // Light Yellow
  JOURNALIST: '#F1948A', // Soft Red
  PRESENTER: '#C39BD3', // Soft Purple
  PHOTOGRAPHER: '#7FB3D5', // Light Blue
  ARCHAEOLOGIST: '#76D7C4', // Medium Sea Green
  CONDUCTOR: '#F7DC6F', // Light Goldenrod
  COMEDIAN: '#85C1E9', // Sky Blue
  PRODUCER: '#BB8FCE', // Medium Purple
  DESIGNER: '#F0B27A', // Light Orange
  ARTIST: '#52BE80', // Medium Sea Green
  DANCER: '#E59866', // Soft Orange
  ANTHROPOLOGIST: '#FAD7A0', // Peach
  LAWYER: '#CD6155', // Indian Red
  GEOGRAPHER: '#F5CBA7', // Soft Peach
  GEOLOGIST: '#5499C7', // Steel Blue
  AMERICAN_FOOTBALL_PLAYER: '#48C9B0', // Medium Turquoise
  SOCIOLOGIST: '#F7F9F9', // Whisper
  MAFIOSO: '#B03A2E', // Dark Red
  DIPLOMAT: '#AAB7B8', // Cadet Grey
  PILOT: '#E6B0AA', // Pastel Pink
  JUDGE: '#1F618D', // Dark Blue
  FASHION_DESIGNER: '#7DCEA0', // Medium Spring Green
  OCCULTIST: '#F5B7B1', // Light Red
  POLITICAL_SCIENTIST: '#154360', // Dark Blue
  PIRATE: '#7D6608', // Dark Gold
  PUBLIC_WORKER: '#76448A', // Dark Medium Purple
  CELEBRITY: '#1ABC9C', // Jade
  MAGICIAN: '#2E4053', // Dark Slate Gray
  STATISTICIAN: '#45B39D', // Medium Aquamarine
  INSPIRATION: '#34495E', // Dark Slate Blue
  CHEF: '#58D68D', // Light Green
  CRITIC: '#5DADE2', // Soft Blue
  MOUNTAINEER: '#F4D03F', // Sunflower Yellow
  BULLFIGHTER: '#EB984E', // Pumpkin Orange
};

export const defaultColor = '#95a5a6'; // Light Gray as a fallback

export const getOccupationColor = (occupation) => {
  const formattedOccupation = occupation.replace(/\s+/g, '_').toUpperCase();
  return occupationColors[formattedOccupation] || defaultColor;
};
